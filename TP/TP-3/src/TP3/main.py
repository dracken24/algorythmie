from TP3.library import Library

def main():
    print("=== SYSTEME DE GESTION DE BIBLIOTHEQUE ===")
    print()
    
    # Création de la bibliothèque avec injection de dépendances (DIP)
    library = Library()
    
    print("\n--- Ajout de livres ---")
    library.add_book("1989", "George Orwell", "978-0123456789", "Fiction")
    library.add_book("Clean Code", "Robert Martin", "978-9876543210", "Informatique")
    library.add_book("Design Patterns", "Gang of Four", "978-1111111111", "Informatique")
    
    print("\n--- Ajout d'utilisateurs ---")
    library.add_user("Alice Martin", "alice@example.com", "student")
    library.add_user("Prof. Dupont", "dupont@example.com", "teacher")
    library.add_user("Admin", "admin@example.com", "admin")
    
    print("\n--- Emprunts ---")
    library.borrow_book(1, 1)  # Alice emprunte 1989
    library.borrow_book(2, 2)  # Prof. Dupont emprunte Clean Code
    
    print("\n--- Recherche ---")
    results = library.search_books("Clean", "title")
    print(f"Résultats de recherche: {len(results)} livre(s) trouvé(s)")
    
    print("\n--- Rapport des retards ---")
    library.generate_overdue_report()

if __name__ == "__main__":
    main()