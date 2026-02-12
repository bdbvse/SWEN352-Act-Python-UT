"""
Filename: run_books_api_samples.py
Description: A simple script to drive the Ext API component.
"""
from library.library import Library
from library.patron import Patron


def main():
    """
    A simple script to exercise the BookService component.
    """
    # Start from a clean slate
    library_svc = Library(start_clean=True)
    # Register a new patron
    bryan = library_svc.register_patron('Bryan', 'Basham', 61, '47')
    # Show that patron's info
    show_a_patron(bryan)
    # Borrow a couple of books
    library_svc.borrow_book(bryan, 'Python')
    library_svc.borrow_book(bryan, 'Clean Code')
    # Show that patron's info
    show_a_patron(bryan)
    # Return a book
    library_svc.return_borrowed_book(bryan, 'Python')
    # Show that patron's info
    show_a_patron(bryan)
    # Shutdown the Service
    library_svc.shutdown()

def show_a_patron(patron: Patron) -> None:
    if len(patron.borrowed_books) == 0:
        print(f"{patron.fname} {patron.lname} has no borrowed books.")
    else:
        print(f"{patron.fname} {patron.lname} has borrowed {len(patron.borrowed_books)} books:")
        for book in patron.borrowed_books:
            print(f"\t{book}")

if __name__ == "__main__":
    main()
