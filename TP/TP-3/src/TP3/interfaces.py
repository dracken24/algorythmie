from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from datetime import datetime

# Interface pour les notifications
class INotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

# Interface pour les observateurs
class IObserver(ABC):
    @abstractmethod
    def update(self, subject: 'ISubject', event_type: str, data: Any) -> None:
        pass

# Interface pour les sujets
class ISubject(ABC):
    @abstractmethod
    def attach(self, observer: IObserver) -> None:
        pass
    
    @abstractmethod
    def detach(self, observer: IObserver) -> None:
        pass
    
    @abstractmethod
    def notify(self, event_type: str, data: Any) -> None:
        pass

# Interface pour la gestion des livres
class IBookRepository(ABC):
    @abstractmethod
    def add_book(self, book_data: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def remove_book(self, book_id: int) -> bool:
        pass
    
    @abstractmethod
    def get_book(self, book_id: int) -> Optional[Dict[str, Any]]:
        pass
    
    @abstractmethod
    def get_all_books(self) -> List[Dict[str, Any]]:
        pass
    
    @abstractmethod
    def update_book_availability(self, book_id: int, available: bool) -> bool:
        pass

# Interface pour la gestion des utilisateurs
class IUserRepository(ABC):
    @abstractmethod
    def add_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def get_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        pass
    
    @abstractmethod
    def get_all_users(self) -> List[Dict[str, Any]]:
        pass

# Interface pour la gestion des emprunts
class ILoanRepository(ABC):
    @abstractmethod
    def add_loan(self, loan_data: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def get_loan(self, loan_id: int) -> Optional[Dict[str, Any]]:
        pass
    
    @abstractmethod
    def get_user_loans(self, user_id: int) -> List[Dict[str, Any]]:
        pass
    
    @abstractmethod
    def update_loan_return(self, loan_id: int, return_date: str) -> bool:
        pass
    
    @abstractmethod
    def get_overdue_loans(self) -> List[Dict[str, Any]]:
        pass

# Interface pour les stratégies de recherche
class ISearchStrategy(ABC):
    @abstractmethod
    def search(self, books: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
        pass

# Interface pour les types d'utilisateurs
class IUserType(ABC):
    @abstractmethod
    def get_max_loans(self) -> int:
        pass
    
    @abstractmethod
    def get_loan_duration(self) -> int:
        pass
    
    @abstractmethod
    def get_type_name(self) -> str:
        pass

# Interface pour les règles d'emprunt
class ILoanRule(ABC):
    @abstractmethod
    def can_borrow(self, user: Dict[str, Any], current_loans: List[Dict[str, Any]]) -> bool:
        pass
    
    @abstractmethod
    def get_error_message(self) -> str:
        pass
