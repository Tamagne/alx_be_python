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
        # Return a string representation of the 
