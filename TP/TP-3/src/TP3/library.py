
import datetime
from TP3.interfaces import INotificationService
from TP3.depots import BookDepot, UserDepot, LoanDepot
from TP3.services import BookService, UserService, LoanService, ReportService
from TP3.observer import ObserverService

# Classe principale pour la gestion de la bibliotheque
# Permet d'injecter les dependances et de creer les services specifiques
class Library:
    def __init__(self, notification_service: INotificationService = None):
        # Injection de dépendances
        if notification_service is None:
            observer_service = ObserverService()
        
        # Creation des repositories
        self.book_depot = BookDepot()
        self.user_depot = UserDepot()
        self.loan_depot = LoanDepot()
        
        # Creation des services specialises
        self.book_service = BookService(self.book_depot, observer_service)
        self.user_service = UserService(self.user_depot, observer_service)
        self.loan_service = LoanService(
            self.book_depot, 
            self.user_depot, 
            self.loan_depot, 
            observer_service
        )
        self.report_service = ReportService(
            self.loan_depot,
            self.user_depot,
            self.book_depot,
            observer_service
        )
    
    # Methods delegated to the appropriate services
    def add_book(self, title: str, author: str, isbn: str, category: str):
        return self.book_service.add_book(title, author, isbn, category)
    
	# Supprimer un livre
    def remove_book(self, book_id: int):
        return self.book_service.remove_book(book_id)
    
	# Ajouter un utilisateur
    def add_user(self, name: str, email: str, user_type: str):
        return self.user_service.add_user(name, email, user_type)
    
	# Emprunter un livre
    def borrow_book(self, user_id: int, book_id: int):
        return self.loan_service.borrow_book(user_id, book_id)
    
	# Retourner un livre
    def return_book(self, loan_id: int):
        return self.loan_service.return_book(loan_id)
    
	# Rechercher des livres
    def search_books(self, search_term: str, search_type: str = 'title'):
        return self.book_service.search_books(search_term, search_type)
    
	# Generer un rapport sur les emprunts en retard
    def generate_overdue_report(self):
        return self.report_service.generate_overdue_report()
