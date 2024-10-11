class Book:
    """Base class for different types of books."""
    
    def __init__(self, title, author):
        """Initialize the book with a title and an author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return a user-friendly string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    
    def __init__(self, title, author, file_size):
        """
        Initialize the EBook with title, author, and file size.
        
        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The size of the e-book file in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the e-book with file size."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""
    
    def __init__(self, title, author, page_count):
        """
        Initialize the PrintBook with title, author, and page count.
        
        Args:
            title (str): The title of the printed book.
            author (str): The author of the printed book.
            page_count (int): The number of pages in the printed book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the printed book with page count."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library that holds a collection of books."""
    
    def __init__(self):
        """Initialize an empty collection of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library collection."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book (or its subclasses) can be added.")

    def list_books(self):
        """List all the books in the library."""
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)