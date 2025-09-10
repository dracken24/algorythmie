from TP3.library import Library

def main():
    print("=== SYSTEME DE GESTION DE BIBLIOTHEQUE ===")
    print()
    
    # Creation of the library with dependency injection
    library = Library()
    
    print("\n--- Add books ---")
    library.add_book("1989", "Tony Orwell", "978-0123456789", "Fiction")
    library.add_book("Clean Code", "Robert Martin", "978-9876543210", "Informatique")
    library.add_book("Design Patterns", "Gang of Four", "978-1111111111", "Informatique")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-2222222222", "Fiction")
    library.add_book("The Catcher in the Rye", "J.D. Salinger", "978-3333333333", "Fiction")
    library.add_book("To Kill a Mockingbird", "Harper Lee", "978-4444444444", "Fiction")
    library.add_book("1984", "Tony Orwell", "978-5555555555", "Fiction")
    library.add_book("The Hobbit", "J.R.R. Tolkien", "978-6666666666", "Fiction")
    library.add_book("The Little Prince", "Antoine de Saint-Exupéry", "978-7777777777", "Fiction")
    library.add_book("The Alchemist", "Paulo Coelho", "978-8888888888", "Fiction")
    
    print("\n--- Add users ---")
    library.add_user("Alice Martin", "alice@example.com", "student")
    library.add_user("Prof. Dupont", "dupont@example.com", "teacher")
    library.add_user("Admin", "admin@example.com", "admin")
    library.add_user("John Tremblay", "john@example.com", "student")
    
    print("\n--- Borrow books ---")
    library.borrow_book(1, 1)  # Alice emprunte 1989
    library.borrow_book(2, 2)  # Prof. Dupont emprunte Clean Code
    library.borrow_book(3, 3)  # Admin emprunte Design Patterns

    print("\n--- Search ---")
    results = library.search_books("Clean", "title")
    print(f"Search results: {len(results)} book(s) found")
    
    print("\n--- Overdue report ---")
    library.generate_overdue_report()

if __name__ == "__main__":
    main()