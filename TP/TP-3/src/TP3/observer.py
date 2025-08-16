from abc import ABC, abstractmethod
from typing import List, Any
from TP3.interfaces import INotificationService, IObserver, ISubject

# Implémentation du pattern Observateur
class Observer(ISubject):
    def __init__(self):
        self._observers: List[IObserver] = []
    
    def attach(self, observer: IObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, event_type: str, data: Any) -> None:
        for observer in self._observers:
            observer.update(self, event_type, data)

# Observateurs presents dans le code
class EmailNotifier(IObserver):
    def update(self, subject: ISubject, event_type: str, data: Any) -> None:
        print(f"EMAIL: {data}")

class SMSNotifier(IObserver):
    def update(self, subject: ISubject, event_type: str, data: Any) -> None:
        print(f"SMS: {data}")

class PushNotifier(IObserver):
    def update(self, subject: ISubject, event_type: str, data: Any) -> None:
        print(f"PUSH: {data}")

class OverdueNotifier(IObserver):
    def update(self, subject: ISubject, event_type: str, data: Any) -> None:
        if event_type == "overdue":
            print(f"NOTIFICATION RETARD: {data}")

# Service de notification principal (DIP)
# Permet d'ajouter de nouveaux types de notifications sans modifier le code existant (OCP)
class ObserverService(INotificationService):
    def __init__(self):
        self.subject = Observer()
        # Ajout des observateurs par défaut
        self.subject.attach(EmailNotifier())
        self.subject.attach(SMSNotifier())
        self.subject.attach(PushNotifier())
        self.subject.attach(OverdueNotifier())
    
    def send_notification(self, message: str) -> None:
        self.subject.notify("general", message)
    
    def send_overdue_notification(self, overdue_info: str) -> None:
        self.subject.notify("overdue", overdue_info)
    
    def add_observer(self, observer: IObserver) -> None:
        """Permet d'ajouter de nouveaux types de notifications sans modifier le code existant (OCP)"""
        self.subject.attach(observer)
    
    def remove_observer(self, observer: IObserver) -> None:
        self.subject.detach(observer)

