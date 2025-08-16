from dataclasses import dataclass
from datetime import datetime
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
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'category': self.category,
            'available': self.available,
            'added_date': self.added_date
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        return cls(
            id=data['id'],
            title=data['title'],
            author=data['author'],
            isbn=data['isbn'],
            category=data['category'],
            available=data['available'],
            added_date=data['added_date']
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
    
    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        return cls(
            id=data['id'],
            name=data['name'],
            email=data['email'],
            user_type=data['type'],
            registration_date=data['registration_date'],
            active=data['active'],
            max_loans=data['max_loans'],
            loan_duration=data['loan_duration']
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
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Loan':
        return cls(
            id=data['id'],
            user_id=data['user_id'],
            book_id=data['book_id'],
            loan_date=data['loan_date'],
            due_date=data.get('due_date'),
            returned=data['returned'],
            return_date=data.get('return_date')
        )
