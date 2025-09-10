from typing import List, Dict, Any
from TP3.interfaces import ILoanRule

# Regle pour verifier si un utilisateur est actif
class UserActiveRule(ILoanRule):
    # Verifie si l'utilisateur est actif
    def can_borrow(self, user: Dict[str, Any], current_loans: List[Dict[str, Any]]) -> bool:
        return user['active']
    
    # Recupere le message d'erreur
    def get_error_message(self) -> str:
        return "Erreur: Utilisateur inactif"

# Regle pour verifier si un livre est disponible
class BookAvailableRule(ILoanRule):
    # Verifie si le livre est disponible
    def can_borrow(self, user: Dict[str, Any], current_loans: List[Dict[str, Any]]) -> bool:
        # Cette règle nécessite le livre, donc on retourne True et on vérifie ailleurs
        return True
    
    # Recupere le message d'erreur
    def get_error_message(self) -> str:
        return "Erreur: Livre non disponible"

# Regle pour verifier si un utilisateur a atteint le nombre maximum d'emprunts
class MaxLoansRule(ILoanRule):
    # Verifie si l'utilisateur a atteint le nombre maximum d'emprunts
    def can_borrow(self, user: Dict[str, Any], current_loans: List[Dict[str, Any]]) -> bool:
        if user['max_loans'] == -1:  # illimité
            return True
        return len(current_loans) < user['max_loans']
    
    # Recupere le message d'erreur
    def get_error_message(self) -> str:
        return "Erreur: Limite d'emprunts atteinte"

# Moteur de regles d'emprunt
class LoanRuleEngine:
    def __init__(self):
        self.rules = [
            UserActiveRule(),
            MaxLoansRule()
        ]

    # Verifie si un utilisateur peut emprunter un livre
    def can_borrow(self, user: Dict[str, Any], current_loans: List[Dict[str, Any]]) -> tuple[bool, str]:
        for rule in self.rules:
            if not rule.can_borrow(user, current_loans):
                return False, rule.get_error_message()
        return True, ""

    # Ajoute une nouvelle regle
    def add_rule(self, rule: ILoanRule) -> None:
        """Permet d'ajouter de nouvelles règles sans modifier le code existant"""
        self.rules.append(rule)
