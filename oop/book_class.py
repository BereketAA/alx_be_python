class Book:
    """A class to represent a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """
        Initialize the book with title, author, and year.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message when the Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return a formal string representation that can recreate the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("Brave New World", "Aldous Huxley", 1932)

    # Print using __str__ and __repr__
    print(book1)  # Expected: 1984 by George Orwell, published in 1949
    print(repr(book1))  # Expected: Book('1984', 'George Orwell', 1949)

    # Trigger __del__ by explicitly deleting the book
    del book1  # Expected: Deleting 1984
    del book2  # Deleting Brave New World (optional in this case)
    