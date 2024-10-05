class Book:
    """A class to represent a book in the library."""

    def __init__(self, title, author):
        """Initialize the book with a title and author."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"

    def check_out(self):
        """Check out the book if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False

    def return_book(self):
        """Return the book to the library."""
        self._is_checked_out = False


class Library:
    """A class to represent a library that holds books."""

    def __init__(self):
        """Initialize an empty list of books."""
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"You have checked out '{title}'."
                else:
                    return f"Sorry, '{title}' is currently checked out."
        return f"'{title}' not found in the library."

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return f"You have returned '{title}'."
        return f"'{title}' not found in the library."

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [str(book) for book in self._books if not book._is_checked_out]
        if not available_books:
            return "No books are currently available in the library."
        return "\n".join(available_books)