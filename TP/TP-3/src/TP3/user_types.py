from TP3.interfaces import IUserType

class StudentType(IUserType):
    def get_max_loans(self) -> int:
        return 3
    
    def get_loan_duration(self) -> int:
        return 14
    
    def get_type_name(self) -> str:
        return "student"

class TeacherType(IUserType):
    def get_max_loans(self) -> int:
        return 10
    
    def get_loan_duration(self) -> int:
        return 30
    
    def get_type_name(self) -> str:
        return "teacher"

class AdminType(IUserType):
    def get_max_loans(self) -> int:
        return -1  # illimité
    
    def get_loan_duration(self) -> int:
        return -1  # illimité
    
    def get_type_name(self) -> str:
        return "admin"

class UserTypeFactory:
    _types = {
        "student": StudentType(),
        "teacher": TeacherType(),
        "admin": AdminType()
    }
    
    @classmethod
    def get_user_type(cls, type_name: str) -> IUserType:
        if type_name not in cls._types:
            raise ValueError(f"Type d'utilisateur invalide: {type_name}")
        return cls._types[type_name]
    
    @classmethod
    def register_user_type(cls, type_name: str, user_type: IUserType) -> None:
        """Permet d'ajouter de nouveaux types d'utilisateurs sans modifier le code existant (OCP)"""
        cls._types[type_name] = user_type
