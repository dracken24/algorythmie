from abc import ABC, abstractmethod
from typing import List, Any
from TP3.interfaces import INotificationService, IObserver, ISubject

# Implementation of the Observer pattern
class Observer(ISubject):
    def __init__(self):
        self._observers: List[IObserver] = []
    
	# Attacher un observateur
    def attach(self, observer: IObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
    
	# Detacher un observateur
    def detach(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
    
	# Notifier les observateurs
    def notify(self, event_type: str, data: Any) -> None:
        for observer in self._observers:
            observer.update(self, event_type, data)

# Observers present in the code

# Notifie par email
class EmailNotifier(IObserver):
	# Mise a jour des observateurs
    def update(self, subject: ISubject, event_type: str, data: Any) -> None:
        print(f"EMAIL: {data}")

# Notifie par SMS
class SMSNotifier(IObserver):
    def update(self, subject: ISubject, event_type: str, data: Any) -> None:
        print(f"SMS: {data}")

# Notifie par Push
class PushNotifier(IObserver):
    def update(self, subject: ISubject, event_type: str, data: Any) -> None:
        print(f"PUSH: {data}")

# Notifie par email pour les emprunts en retard
class OverdueNotifier(IObserver):
    def update(self, subject: ISubject, event_type: str, data: Any) -> None:
        if event_type == "overdue":
            print(f"NOTIFICATION RETARD: {data}")

# Main notification service
# Allows to add new notification types without modifying the existing code
class ObserverService(INotificationService):
    def __init__(self):
        self.subject = Observer()
        # Ajout des observateurs par defaut
        self.subject.attach(EmailNotifier())
        self.subject.attach(SMSNotifier())
        self.subject.attach(PushNotifier())
        self.subject.attach(OverdueNotifier())
    
	# Envoi de notification
    def send_notification(self, message: str) -> None:
        self.subject.notify("general", message)
    
	# Envoi de notification pour les emprunts en retard
    def send_overdue_notification(self, overdue_info: str) -> None:
        self.subject.notify("overdue", overdue_info)
    
	# Ajout d'un observateur
    def add_observer(self, observer: IObserver) -> None:
        """Permet d'ajouter de nouveaux types de notifications sans modifier le code existant"""
        self.subject.attach(observer)
    
	# Suppression d'un observateur
    def remove_observer(self, observer: IObserver) -> None:
        self.subject.detach(observer)

