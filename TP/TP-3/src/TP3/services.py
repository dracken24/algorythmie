from typing import List, Dict, Any, Optional
from TP3.interfaces import IBookRepository, IUserRepository, ILoanRepository, INotificationService
from TP3.user_types import UserTypeFactory
from TP3.search_strategies import SearchStrategyFactory
from TP3.loan_rules import LoanRuleEngine
import datetime

class BookService:
    """Service dédié à la gestion des livres (SRP)"""
    
    def __init__(self, book_repository: IBookRepository, notification_service: INotificationService):
        self.book_repository = book_repository
        self.notification_service = notification_service
    
    def add_book(self, title: str, author: str, isbn: str, category: str) -> Dict[str, Any]:
        book_data = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'category': category
        }
        book = self.book_repository.add_book(book_data)
        self.notification_service.send_notification(f"Nouveau livre ajouté - {title}")
        return book
    
    def remove_book(self, book_id: int) -> bool:
        success = self.book_repository.remove_book(book_id)
        if success:
            self.notification_service.send_notification(f"Livre supprimé - ID {book_id}")
        return success
    
    def search_books(self, search_term: str, search_type: str = 'title') -> List[Dict[str, Any]]:
        try:
            strategy = SearchStrategyFactory.get_strategy(search_type)
            books = self.book_repository.get_all_books()
            return strategy.search(books, search_term)
        except ValueError:
            print("Type de recherche invalide")
            return []

class UserService:
    """Service dédié à la gestion des utilisateurs (SRP)"""
    
    def __init__(self, user_repository: IUserRepository, notification_service: INotificationService):
        self.user_repository = user_repository
        self.notification_service = notification_service
    
    def add_user(self, name: str, email: str, user_type: str) -> Dict[str, Any]:
        user_type_obj = UserTypeFactory.get_user_type(user_type)
        user_data = {
            'name': name,
            'email': email,
            'user_type': user_type,
            'max_loans': user_type_obj.get_max_loans(),
            'loan_duration': user_type_obj.get_loan_duration()
        }
        user = self.user_repository.add_user(user_data)
        self.notification_service.send_notification(f"Nouvel utilisateur ajouté - {name}")
        return user

class LoanService:
    """Service dédié à la gestion des emprunts (SRP)"""
    
    def __init__(self, 
                book_repository: IBookRepository,
                user_repository: IUserRepository,
                loan_repository: ILoanRepository,
                notification_service: INotificationService):
        self.book_repository = book_repository
        self.user_repository = user_repository
        self.loan_repository = loan_repository
        self.notification_service = notification_service
        self.rule_engine = LoanRuleEngine()
    
    def borrow_book(self, user_id: int, book_id: int) -> bool:
        user = self.user_repository.get_user(user_id)
        book = self.book_repository.get_book(book_id)
        
        if not user or not book:
            print("Erreur: Utilisateur ou livre introuvable")
            return False
        
        if not book['available']:
            print("Erreur: Livre non disponible")
            return False
        
        current_loans = self.loan_repository.get_user_loans(user_id)
        can_borrow, error_message = self.rule_engine.can_borrow(user, current_loans)
        
        if not can_borrow:
            print(error_message)
            return False
        
        # Calcul de la date d'échéance
        user_type_obj = UserTypeFactory.get_user_type(user['type'])
        due_date = None
        if user_type_obj.get_loan_duration() != -1:
            due_date = (datetime.datetime.now() + 
                       datetime.timedelta(days=user_type_obj.get_loan_duration())).isoformat()
        
        loan_data = {
            'user_id': user_id,
            'book_id': book_id,
            'loan_date': datetime.datetime.now().isoformat(),
            'due_date': due_date
        }
        
        self.loan_repository.add_loan(loan_data)
        self.book_repository.update_book_availability(book_id, False)
        
        self.notification_service.send_notification(
            f"Emprunt effectué - Livre: {book['title']}, Utilisateur: {user['name']}"
        )
        
        return True
    
    def return_book(self, loan_id: int) -> bool:
        loan = self.loan_repository.get_loan(loan_id)
        if not loan:
            print("Erreur: Emprunt introuvable")
            return False
        
        if loan['returned']:
            print("Erreur: Livre déjà retourné")
            return False
        
        return_date = datetime.datetime.now().isoformat()
        success = self.loan_repository.update_loan_return(loan_id, return_date)
        
        if success:
            self.book_repository.update_book_availability(loan['book_id'], True)
            self.notification_service.send_notification(f"Retour effectué - ID Emprunt: {loan_id}")
        
        return success

class ReportService:
    """Service dédié à la génération de rapports (SRP)"""
    
    def __init__(self, 
                 loan_repository: ILoanRepository,
                 user_repository: IUserRepository,
                 book_repository: IBookRepository,
                 notification_service: INotificationService):
        self.loan_repository = loan_repository
        self.user_repository = user_repository
        self.book_repository = book_repository
        self.notification_service = notification_service
    
    def generate_overdue_report(self) -> List[Dict[str, Any]]:
        overdue_loans = self.loan_repository.get_overdue_loans()
        current_date = datetime.datetime.now()
        
        detailed_overdue = []
        for loan in overdue_loans:
            user = self.user_repository.get_user(loan['user_id'])
            book = self.book_repository.get_book(loan['book_id'])
            
            if user and book and loan['due_date']:
                due_date = datetime.datetime.fromisoformat(loan['due_date'])
                days_overdue = (current_date - due_date).days
                
                overdue_info = {
                    'loan': loan,
                    'user': user,
                    'book': book,
                    'days_overdue': days_overdue
                }
                detailed_overdue.append(overdue_info)
        
        if detailed_overdue:
            print(f"RAPPORT: {len(detailed_overdue)} emprunts en retard")
            for overdue in detailed_overdue:
                print(f"- {overdue['book']['title']} par {overdue['user']['name']} "
                      f"({overdue['days_overdue']} jours de retard)")
                
                # Utilisation du pattern Observateur pour les notifications de retard
                self.notification_service.send_overdue_notification(
                    f"Retard: {overdue['book']['title']} - {overdue['days_overdue']} jours"
                )
        
        return detailed_overdue
