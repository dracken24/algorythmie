
import datetime
from TP3.interfaces import INotificationService
from TP3.repositories import BookRepository, UserRepository, LoanRepository
from TP3.services import BookService, UserService, LoanService, ReportService
from TP3.observer import ObserverService

class Library:
    """
    Classe Library refactorisée selon les principes SOLID:
    - SRP: Délègue les responsabilités aux services spécialisés
    - OCP: Ouverte à l'extension via les interfaces
    - LSP: Utilise les interfaces abstraites
    - ISP: Interfaces spécialisées pour chaque responsabilité
    - DIP: Dépend des abstractions, pas des implémentations concrètes
    """
    
    def __init__(self, notification_service: INotificationService = None):
        # Injection de dépendances (DIP)
        if notification_service is None:
            observer_service = ObserverService()
        
        # Création des repositories
        self.book_repository = BookRepository()
        self.user_repository = UserRepository()
        self.loan_repository = LoanRepository()
        
        # Création des services spécialisés (SRP)
        self.book_service = BookService(self.book_repository, observer_service)
        self.user_service = UserService(self.user_repository, observer_service)
        self.loan_service = LoanService(
            self.book_repository, 
            self.user_repository, 
            self.loan_repository, 
            observer_service
        )
        self.report_service = ReportService(
            self.loan_repository,
            self.user_repository,
            self.book_repository,
            observer_service
        )
    
    # Méthodes déléguées aux services appropriés
    def add_book(self, title: str, author: str, isbn: str, category: str):
        return self.book_service.add_book(title, author, isbn, category)
    
    def remove_book(self, book_id: int):
        return self.book_service.remove_book(book_id)
    
    def add_user(self, name: str, email: str, user_type: str):
        return self.user_service.add_user(name, email, user_type)
    
    def borrow_book(self, user_id: int, book_id: int):
        return self.loan_service.borrow_book(user_id, book_id)
    
    def return_book(self, loan_id: int):
        return self.loan_service.return_book(loan_id)
    
    def search_books(self, search_term: str, search_type: str = 'title'):
        return self.book_service.search_books(search_term, search_type)
    
    def generate_overdue_report(self):
        return self.report_service.generate_overdue_report()
