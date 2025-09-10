from dataclasses import dataclass
from typing import Optional

# Class qui represente un livre
@dataclass
class Book:
    id: int
    title: str
    author: str
    isbn: str
    category: str
    available: bool
    added_date: str
    
	# Convertir en dictionnaire
    def to_dict(self) -> dict:
        return{
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'category': self.category,
            'available': self.available,
            'added_date': self.added_date
        }
    
	# Convertir depuis un dictionnaire
    @classmethod
    def from_dict(cls, infos: dict) -> 'Book':
        return cls(
            id=infos['id'],
            title=infos['title'],
            author=infos['author'],
            isbn=infos['isbn'],
            category=infos['category'],
            available=infos['available'],
            added_date=infos['added_date']
        )

# Class qui represente un utilisateur
@dataclass
class User:
    id: int
    name: str
    email: str
    user_type: str
    registration_date: str
    active: bool
    max_loans: int
    loan_duration: int
    
	# Convertir en dictionnaire
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'type': self.user_type,
            'registration_date': self.registration_date,
            'active': self.active,
            'max_loans': self.max_loans,
            'loan_duration': self.loan_duration
        }
    
	# Convertir depuis un dictionnaire
    @classmethod
    def from_dict(cls, infos: dict) -> 'User':
        return cls(
            id=infos['id'],
            name=infos['name'],
            email=infos['email'],
            user_type=infos['type'],
            registration_date=infos['registration_date'],
            active=infos['active'],
            max_loans=infos['max_loans'],
            loan_duration=infos['loan_duration']
        )

# Class qui represente un emprunt
@dataclass
class Loan:
    id: int
    user_id: int
    book_id: int
    loan_date: str
    due_date: Optional[str]
    returned: bool
    return_date: Optional[str]
    
	# Convertir en dictionnaire
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'loan_date': self.loan_date,
            'due_date': self.due_date,
            'returned': self.returned,
            'return_date': self.return_date
        }
    
	# Convertir depuis un dictionnaire
    @classmethod
    def from_dict(cls, infos: dict) -> 'Loan':
        return cls(
            id=infos['id'],
            user_id=infos['user_id'],
            book_id=infos['book_id'],
            loan_date=infos['loan_date'],
            due_date=infos.get('due_date'),
            returned=infos['returned'],
            return_date=infos.get('return_date')
        )
