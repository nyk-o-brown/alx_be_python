class Book:
    def __init__(self, title, author):
        
       self.title = title
       self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)
               
class Library:
    def __init__(self):
        self.books = []  # will hold Book, EBook, PrintBook instances

    def add_book(self, book):
        """Add any Book-derived object to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            # Decide how to display based on the book’s class
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")

                      