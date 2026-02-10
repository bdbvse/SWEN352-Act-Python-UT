"""
Filename: run_books_api_samples.py
Description: A simple script to drive the Ext API component.
"""

from library.library_db_interface import Library_DB
from library.patron import Patron


def main():
    """
    A simple script to exercise the BookService component.
    """
    # Start from a clean slate
    library_svc = Library_DB(start_clean=True)
    # Create a new patron
    bryan = Patron('Bryan', 'Basham', 61, '47')
    library_svc.insert_patron(bryan)
    # Show that patron's info
    show_a_patron(bryan)
    # Update patron's info
    updated_patron = bryan.with_age(21)
    library_svc.update_patron(updated_patron)
    # Show that patron's info
    show_a_patron(library_svc.retrieve_patron(bryan.member_id))
    # Shutdown the database connection
    library_svc.db.close()

def show_a_patron(patron: Patron) -> None:
    print(f"Patron {patron.member_id} is {patron.fname} {patron.lname} and is {patron.age} years old")

if __name__ == "__main__":
    main()
