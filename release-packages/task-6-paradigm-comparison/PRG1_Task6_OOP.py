"""
Library Book Tracker (Object-Oriented Version)

Tracks a small collection of library books: which ones are checked
out, and which are available. This version uses a Book class and a
Library class.

This program is complete and working. Read it alongside
PRG1_Task6_Procedural.py; you are not asked to change or submit
either file.
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def check_out(self):
        """Mark this book as checked out. Return True if successful."""
        if not self.checked_out:
            self.checked_out = True
            return True
        return False

    def return_book(self):
        """Mark this book as returned. Return True if successful."""
        if self.checked_out:
            self.checked_out = False
            return True
        return False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        """Add a new book to the collection, available by default."""
        self.books.append(Book(title, author))

    def check_out_book(self, title):
        """Check out the first available book matching this title."""
        for book in self.books:
            if book.title == title and not book.checked_out:
                return book.check_out()
        return False

    def return_book(self, title):
        """Return the first checked-out book matching this title."""
        for book in self.books:
            if book.title == title and book.checked_out:
                return book.return_book()
        return False

    def list_available_books(self):
        """Return a list of titles for every book that is not checked out."""
        available = []
        for book in self.books:
            if not book.checked_out:
                available.append(book.title)
        return available


if __name__ == "__main__":
    library = Library()
    library.add_book("Fahrenheit 451", "Ray Bradbury")
    library.add_book("Kindred", "Octavia Butler")
    library.add_book("The Left Hand of Darkness", "Ursula K. Le Guin")

    library.check_out_book("Kindred")

    print("Available books:")
    for title in library.list_available_books():
        print(f"- {title}")

    library.return_book("Kindred")

    print("Available books after return:")
    for title in library.list_available_books():
        print(f"- {title}")
