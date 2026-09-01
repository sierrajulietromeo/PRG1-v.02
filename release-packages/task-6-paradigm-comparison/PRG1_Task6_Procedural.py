"""
Library Book Tracker (Procedural Version)

Tracks a small collection of library books: which ones are checked
out, and which are available. This version uses a list of
dictionaries to represent the books.

This program is complete and working. Read it alongside
PRG1_Task6_OOP.py; you are not asked to change or submit either file.
"""


def add_book(books, title, author):
    """Add a new book to the collection, available by default."""
    book = {"title": title, "author": author, "checked_out": False}
    books.append(book)


def check_out_book(books, title):
    """Mark a book as checked out. Return True if successful."""
    for book in books:
        if book["title"] == title and not book["checked_out"]:
            book["checked_out"] = True
            return True
    return False


def return_book(books, title):
    """Mark a book as returned. Return True if successful."""
    for book in books:
        if book["title"] == title and book["checked_out"]:
            book["checked_out"] = False
            return True
    return False


def list_available_books(books):
    """Return a list of titles for every book that is not checked out."""
    available = []
    for book in books:
        if not book["checked_out"]:
            available.append(book["title"])
    return available


if __name__ == "__main__":
    books = []
    add_book(books, "Fahrenheit 451", "Ray Bradbury")
    add_book(books, "Kindred", "Octavia Butler")
    add_book(books, "The Left Hand of Darkness", "Ursula K. Le Guin")

    check_out_book(books, "Kindred")

    print("Available books:")
    for title in list_available_books(books):
        print(f"- {title}")

    return_book(books, "Kindred")

    print("Available books after return:")
    for title in list_available_books(books):
        print(f"- {title}")
