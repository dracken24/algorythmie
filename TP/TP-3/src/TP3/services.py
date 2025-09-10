from typing import List, Dict, Any, Optional
from TP3.interfaces import IBookDepot, IUserDepot, ILoanDepot, INotificationService
from TP3.user_types import UserTypeFactory
from TP3.search_strategies import SearchFactory
from TP3.loan_rules import LoanRuleEngine
import datetime

# Service pour la gestion des livres
class BookService:
    """Service dedie a la gestion des livres"""
    
    def __init__(self, book_depot: IBookDepot, notification_service: INotificationService):
        self.book_depot = book_depot
        self.notification_service = notification_service
    
	# Ajouter un livre
    def add_book(self, title: str, author: str, isbn: str, category: str) -> Dict[str, Any]:
        book_data = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'category': category
        }
        book = self.book_depot.add_book(book_data)
        self.notification_service.send_notification(f"Nouveau livre ajoute - {title}")
        return book
    
	# Supprimer un livre
    def remove_book(self, book_id: int) -> bool:
        success = self.book_depot.remove_book(book_id)
        if success:
            self.notification_service.send_notification(f"Livre supprime - ID {book_id}")
        return success
    
	# Rechercher des livres
    def search_books(self, search_term: str, search_type: str = 'title') -> List[Dict[str, Any]]:
        try:
            strategy = SearchFactory.get_search(search_type)
            books = self.book_depot.get_all_books()
            return strategy.search(books, search_term)
        except ValueError:
            print("Type de recherche invalide")
            return []

# Service pour la gestion des utilisateurs
class UserService:
    """Service dedie a la gestion des utilisateurs"""
    
    def __init__(self, user_depot: IUserDepot, notification_service: INotificationService):
        self.user_depot = user_depot
        self.notification_service = notification_service
    
	# Ajouter un utilisateur
    def add_user(self, name: str, email: str, user_type: str) -> Dict[str, Any]:
        user_type_obj = UserTypeFactory.get_user_type(user_type)
        user_data = {
            'name': name,
            'email': email,
            'user_type': user_type,
            'max_loans': user_type_obj.get_max_loans(),
            'loan_duration': user_type_obj.get_loan_duration()
        }
        user = self.user_depot.add_user(user_data)
        self.notification_service.send_notification(f"Nouvel utilisateur ajouté - {name}")
        return user

# Service pour la gestion des emprunts
class LoanService:
    """Service dedie a la gestion des emprunts"""
    
    def __init__(self, 
                book_depot: IBookDepot,
                user_depot: IUserDepot,
                loan_depot: ILoanDepot,
                notification_service: INotificationService):
        self.book_depot = book_depot
        self.user_depot = user_depot
        self.loan_depot = loan_depot
        self.notification_service = notification_service
        self.rule_engine = LoanRuleEngine()
    
	# Emprunter un livre
    def borrow_book(self, user_id: int, book_id: int) -> bool:
        user = self.user_depot.get_user(user_id)
        book = self.book_depot.get_book(book_id)
        
        if not user or not book:
            print("Erreur: Utilisateur ou livre introuvable")
            return False
        
        if not book['available']:
            print("Erreur: Livre non disponible")
            return False
        
        current_loans = self.loan_depot.get_user_loans(user_id)
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
        
        self.loan_depot.add_loan(loan_data)
        self.book_depot.update_book_availability(book_id, False)
        
        self.notification_service.send_notification(
            f"Emprunt effectué - Livre: {book['title']}, Utilisateur: {user['name']}"
        )
        
        return True
    
	# Retourner un livre
    def return_book(self, loan_id: int) -> bool:
        loan = self.loan_depot.get_loan(loan_id)
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

# Service pour la generation de rapports
class ReportService:
    """Service dedie a la generation de rapports"""
    
    def __init__(self, 
                loan_depot: ILoanDepot,
                user_depot: IUserDepot,
                book_depot: IBookDepot,
                notification_service: INotificationService):
        self.loan_depot = loan_depot
        self.user_depot = user_depot
        self.book_depot = book_depot
        self.notification_service = notification_service
    
	# Generer un rapport sur les emprunts en retard
    def generate_overdue_report(self) -> List[Dict[str, Any]]:
        overdue_loans = self.loan_depot.get_overdue_loans()
        current_date = datetime.datetime.now()
        
        detailed_overdue = []
        for loan in overdue_loans:
            user = self.user_depot.get_user(loan['user_id'])
            book = self.book_depot.get_book(loan['book_id'])
            
			# Si l'utilisateur, le livre et la date d'echeance existent, on calcule le nombre de jours de retard
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
        
		# Si il y a des emprunts en retard, on les affiche et on notifie par email
        if detailed_overdue:
            print(f"RAPPORT: {len(detailed_overdue)} emprunts en retard")
            for overdue in detailed_overdue:
                print(f"- {overdue['book']['title']} par {overdue['user']['name']} "
                        f"({overdue['days_overdue']} jours de retard)")
                
                # Utilisation du pattern Observer pour les notifications de retard
                self.notification_service.send_overdue_notification(
                    f"Retard: {overdue['book']['title']} - {overdue['days_overdue']} jours"
                )
        
        return detailed_overdue
