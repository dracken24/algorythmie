from typing import List, Dict, Any
from TP3.interfaces import ISearchStrategy

class TitleSearchStrategy(ISearchStrategy):
    def search(self, books: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
        return [book for book in books if search_term.lower() in book['title'].lower()]

class AuthorSearchStrategy(ISearchStrategy):
    def search(self, books: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
        return [book for book in books if search_term.lower() in book['author'].lower()]

class ISBNSearchStrategy(ISearchStrategy):
    def search(self, books: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
        return [book for book in books if search_term in book['isbn']]

class CategorySearchStrategy(ISearchStrategy):
    def search(self, books: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
        return [book for book in books if search_term.lower() in book['category'].lower()]

class SearchStrategyFactory:
    _strategies = {
        'title': TitleSearchStrategy(),
        'author': AuthorSearchStrategy(),
        'isbn': ISBNSearchStrategy(),
        'category': CategorySearchStrategy()
    }
    
    @classmethod
    def get_strategy(cls, search_type: str) -> ISearchStrategy:
        if search_type not in cls._strategies:
            raise ValueError(f"Type de recherche invalide: {search_type}")
        return cls._strategies[search_type]
    
    @classmethod
    def register_strategy(cls, search_type: str, strategy: ISearchStrategy) -> None:
        """Permet d'ajouter de nouvelles stratégies de recherche sans modifier le code existant (OCP)"""
        cls._strategies[search_type] = strategy
