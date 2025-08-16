from typing import List, Optional, Dict, Any
from TP3.interfaces import IBookRepository, IUserRepository, ILoanRepository
from TP3.models import Book, User, Loan
import datetime

class BookRepository(IBookRepository):
    def __init__(self):
        self.books = []
        self.next_id = 1
    
    def add_book(self, book_data: Dict[str, Any]) -> Dict[str, Any]:
        book = Book(
            id=self.next_id,
            title=book_data['title'],
            author=book_data['author'],
            isbn=book_data['isbn'],
            category=book_data['category'],
            available=True,
            added_date=datetime.datetime.now().isoformat()
        )
        self.books.append(book)
        self.next_id += 1
        return book.to_dict()
    
    def remove_book(self, book_id: int) -> bool:
        for i, book in enumerate(self.books):
            if book.id == book_id:
                if not book.available:
                    return False
                del self.books[i]
                return True
        return False
    
    def get_book(self, book_id: int) -> Optional[Dict[str, Any]]:
        for book in self.books:
            if book.id == book_id:
                return book.to_dict()
        return None
    
    def get_all_books(self) -> List[Dict[str, Any]]:
        return [book.to_dict() for book in self.books]
    
    def update_book_availability(self, book_id: int, available: bool) -> bool:
        for book in self.books:
            if book.id == book_id:
                book.available = available
                return True
        return False

class UserRepository(IUserRepository):
    def __init__(self):
        self.users = []
        self.next_id = 1
    
    def add_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        user = User(
            id=self.next_id,
            name=user_data['name'],
            email=user_data['email'],
            user_type=user_data['user_type'],
            registration_date=datetime.datetime.now().isoformat(),
            active=True,
            max_loans=user_data['max_loans'],
            loan_duration=user_data['loan_duration']
        )
        self.users.append(user)
        self.next_id += 1
        return user.to_dict()
    
    def get_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        for user in self.users:
            if user.id == user_id:
                return user.to_dict()
        return None
    
    def get_all_users(self) -> List[Dict[str, Any]]:
        return [user.to_dict() for user in self.users]

class LoanRepository(ILoanRepository):
    def __init__(self):
        self.loans = []
        self.next_id = 1
    
    def add_loan(self, loan_data: Dict[str, Any]) -> Dict[str, Any]:
        loan = Loan(
            id=self.next_id,
            user_id=loan_data['user_id'],
            book_id=loan_data['book_id'],
            loan_date=loan_data['loan_date'],
            due_date=loan_data.get('due_date'),
            returned=False,
            return_date=None
        )
        self.loans.append(loan)
        self.next_id += 1
        return loan.to_dict()
    
    def get_loan(self, loan_id: int) -> Optional[Dict[str, Any]]:
        for loan in self.loans:
            if loan.id == loan_id:
                return loan.to_dict()
        return None
    
    def get_user_loans(self, user_id: int) -> List[Dict[str, Any]]:
        return [loan.to_dict() for loan in self.loans 
                if loan.user_id == user_id and not loan.returned]
    
    def update_loan_return(self, loan_id: int, return_date: str) -> bool:
        for loan in self.loans:
            if loan.id == loan_id:
                loan.returned = True
                loan.return_date = return_date
                return True
        return False
    
    def get_overdue_loans(self) -> List[Dict[str, Any]]:
        current_date = datetime.datetime.now()
        overdue_loans = []
        
        for loan in self.loans:
            if not loan.returned and loan.due_date:
                due_date = datetime.datetime.fromisoformat(loan.due_date)
                if current_date > due_date:
                    overdue_loans.append(loan.to_dict())
        
        return overdue_loans
