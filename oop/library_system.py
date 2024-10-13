class Book:
    def __init__(self, title, author):
        # Initialize the book with a title and author
        self.title = title
        self.author = author

    def __str__(self):
        # Return a string representation of the book
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        # Initialize the EBook with title, author, and file size
        super().__init__(title, author)
        self.file_size = file_size  

    def __str__(self):
        # Return a string representation of the EBook
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Initialize the PrintBook with title, author, and page count
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        # Return a string representation of the PrintBook
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        # Initialize an empty list to hold books in the library
        self.books = [] 

    def add_book(self, book):
        # Add a book to the library
        self.books.append(book)

    def list_books(self):
        # Print the details of all books in the library
        for book in self.books:
            print(book)

# Example usage
if __name__ == "__main__":
    lib = Library()
    book1 = PrintBook("1984", "George Orwell", 328)
    book2 = EBook("Python Programming", "John Doe", 15)

    lib.add_book(book1)
    lib.add_book(book2)
    
    print("Books in the library:")
    lib.list_books()
