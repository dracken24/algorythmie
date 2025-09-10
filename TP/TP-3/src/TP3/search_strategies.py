from typing import List, Dict, Any
from TP3.interfaces import ISearch

# Recherche par titre
class TitleSearch(ISearch):
    # Recherche par titre
    def search(self, books: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
        return [book for book in books if search_term.lower() in book['title'].lower()]

# Recherche par auteur
class AuthorSearch(ISearch):
    # Recherche par auteur
    def search(self, books: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
        return [book for book in books if search_term.lower() in book['author'].lower()]

# Recherche par ISBN
class ISBNSearch(ISearch):
    # Recherche par ISBN
    def search(self, books: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
        return [book for book in books if search_term in book['isbn']]

# Recherche par categorie
class CategorySearch(ISearch):
    # Recherche par categorie
    def search(self, books: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
        return [book for book in books if search_term.lower() in book['category'].lower()]

# Fabrique de recherche
class SearchFactory:
    _strategies = {
        'title': TitleSearch(),
        'author': AuthorSearch(),
        'isbn': ISBNSearch(),
        'category': CategorySearch()
    }
    
	# Recuperer une strategie de recherche
    @classmethod
    def get_search(cls, search_type: str) -> ISearch:
        if search_type not in cls._strategies:
            raise ValueError(f"Type de recherche invalide: {search_type}")
        return cls._strategies[search_type]
    
	# Ajouter une nouvelle strategie de recherche
    @classmethod
    def register_search(cls, search_type: str, search: ISearch) -> None:
        """Permet d'ajouter de nouvelles strategie de recherche sans modifier le code existant"""
        cls._strategies[search_type] = search
