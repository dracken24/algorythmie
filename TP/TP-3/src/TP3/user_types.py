from TP3.interfaces import IUserType

# Type d'utilisateur pour les etudiants
class StudentType(IUserType):
    # Recuperer le nombre maximum d'emprunts
    def get_max_loans(self) -> int:
        return 3
    
    # Recuperer la duree d'emprunt
    def get_loan_duration(self) -> int:
        return 14
    
    # Recuperer le nom du type d'utilisateur
    def get_type_name(self) -> str:
        return "student"

# Type d'utilisateur pour les enseignants
class TeacherType(IUserType):
    # Recuperer le nombre maximum d'emprunts
    def get_max_loans(self) -> int:
        return 10
    
    # Recuperer la duree d'emprunt
    def get_loan_duration(self) -> int:
        return 30
    
    # Recuperer le nom du type d'utilisateur
    def get_type_name(self) -> str:
        return "teacher"

# Type d'utilisateur pour les administrateurs
class AdminType(IUserType):
    # Recuperer le nombre maximum d'emprunts
    def get_max_loans(self) -> int:
        return -1  # illimité
    
    # Recuperer la duree d'emprunt
    def get_loan_duration(self) -> int:
        return -1  # illimité
    
    # Recuperer le nom du type d'utilisateur
    def get_type_name(self) -> str:
        return "admin"

# Fabrique de type d'utilisateur
class UserTypeFactory:
    _types = {
        "student": StudentType(),
        "teacher": TeacherType(),
        "admin": AdminType()
    }
    
    # Recuperer un type d'utilisateur
    @classmethod
    def get_user_type(cls, type_name: str) -> IUserType:
        if type_name not in cls._types:
            raise ValueError(f"Type d'utilisateur invalide: {type_name}")
        return cls._types[type_name]
    
    # Ajouter un nouveau type d'utilisateur
    @classmethod
    def register_user_type(cls, type_name: str, user_type: IUserType) -> None:
        """Permet d'ajouter de nouveaux types d'utilisateurs sans modifier le code existant"""
        cls._types[type_name] = user_type
