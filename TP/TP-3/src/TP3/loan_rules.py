from typing import List, Dict, Any
from TP3.interfaces import ILoanRule

class UserActiveRule(ILoanRule):
    def can_borrow(self, user: Dict[str, Any], current_loans: List[Dict[str, Any]]) -> bool:
        return user['active']
    
    def get_error_message(self) -> str:
        return "Erreur: Utilisateur inactif"

class BookAvailableRule(ILoanRule):
    def can_borrow(self, user: Dict[str, Any], current_loans: List[Dict[str, Any]]) -> bool:
        # Cette règle nécessite le livre, donc on retourne True et on vérifie ailleurs
        return True
    
    def get_error_message(self) -> str:
        return "Erreur: Livre non disponible"

class MaxLoansRule(ILoanRule):
    def can_borrow(self, user: Dict[str, Any], current_loans: List[Dict[str, Any]]) -> bool:
        if user['max_loans'] == -1:  # illimité
            return True
        return len(current_loans) < user['max_loans']
    
    def get_error_message(self) -> str:
        return "Erreur: Limite d'emprunts atteinte"

class LoanRuleEngine:
    def __init__(self):
        self.rules = [
            UserActiveRule(),
            MaxLoansRule()
        ]
    
    def can_borrow(self, user: Dict[str, Any], current_loans: List[Dict[str, Any]]) -> tuple[bool, str]:
        for rule in self.rules:
            if not rule.can_borrow(user, current_loans):
                return False, rule.get_error_message()
        return True, ""
    
    def add_rule(self, rule: ILoanRule) -> None:
        """Permet d'ajouter de nouvelles règles sans modifier le code existant (OCP)"""
        self.rules.append(rule)
