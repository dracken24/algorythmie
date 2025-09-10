from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from datetime import datetime

# Interface pour les notifications
class INotificationService(ABC):
    # Envoi de notification
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

# Interface pour les observateurs
class IObserver(ABC):
    # Mise a jour des observateurs
    @abstractmethod
    def update(self, subject: 'ISubject', event_type: str, data: Any) -> None:
        pass

# Interface pour les sujets
class ISubject(ABC):
    # Attacher un observateur
    @abstractmethod
    def attach(self, observer: IObserver) -> None:
        pass
    
    # Detacher un observateur
    @abstractmethod
    def detach(self, observer: IObserver) -> None:
        pass
    
    # Notifier les observateurs
    @abstractmethod
    def notify(self, event_type: str, data: Any) -> None:
        pass

# Interface pour la gestion des livres
class IBookDepot(ABC):
    # Ajouter un livre
    @abstractmethod
    def add_book(self, book_data: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    # Supprimer un livre
    @abstractmethod
    def remove_book(self, book_id: int) -> bool:
        pass
    
    # Recuperer un livre
    @abstractmethod
    def get_book(self, book_id: int) -> Optional[Dict[str, Any]]:
        pass
    
    # Recuperer tous les livres
    @abstractmethod
    def get_all_books(self) -> List[Dict[str, Any]]:
        pass
    
    # Mettre a jour la disponibilite d'un livre
    @abstractmethod
    def update_book_availability(self, book_id: int, available: bool) -> bool:
        pass

# Interface pour la gestion des utilisateurs
class IUserDepot(ABC):
    # Ajouter un utilisateur
    @abstractmethod
    def add_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    # Recuperer un utilisateur
    @abstractmethod
    def get_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        pass
    
    # Recuperer tous les utilisateurs
    @abstractmethod
    def get_all_users(self) -> List[Dict[str, Any]]:
        pass

# Interface pour la gestion des emprunts
class ILoanDepot(ABC):
    # Ajouter un emprunt
    @abstractmethod
    def add_loan(self, loan_data: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    # Recuperer un emprunt
    @abstractmethod
    def get_loan(self, loan_id: int) -> Optional[Dict[str, Any]]:
        pass
    
    # Recuperer tous les emprunts d'un utilisateur
    @abstractmethod
    def get_user_loans(self, user_id: int) -> List[Dict[str, Any]]:
        pass
    
    # Mettre a jour la date de retour d'un emprunt
    @abstractmethod
    def update_loan_return(self, loan_id: int, return_date: str) -> bool:
        pass
    
    # Recuperer tous les emprunts en retard
    @abstractmethod
    def get_overdue_loans(self) -> List[Dict[str, Any]]:
        pass

# Interface pour les strategies de recherche
class ISearch(ABC):
    # Rechercher des livres
    @abstractmethod
    def search(self, books: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
        pass

# Interface pour les types d'utilisateurs
class IUserType(ABC):
    # Recuperer le nombre maximum d'emprunts
    @abstractmethod
    def get_max_loans(self) -> int:
        pass
    
    # Recuperer la duree d'emprunt
    @abstractmethod
    def get_loan_duration(self) -> int:
        pass
    
    # Recuperer le nom du type d'utilisateur
    @abstractmethod
    def get_type_name(self) -> str:
        pass

# Interface pour les regles d'emprunt
class ILoanRule(ABC):
    # Verifier si un utilisateur peut emprunter un livre
    @abstractmethod
    def can_borrow(self, user: Dict[str, Any], current_loans: List[Dict[str, Any]]) -> bool:
        pass
    
    # Recuperer le message d'erreur
    @abstractmethod
    def get_error_message(self) -> str:
        pass
