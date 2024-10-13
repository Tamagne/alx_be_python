class Book:
    def __init__(self, title, author, year):
        # Initialize the book with a title, author, and year of publication
        self.title = title 
        self.author = author 
        self.year = year      

    def __del__(self):
        # Print a message when the book instance is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # Return a user-friendly string representation of the book
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Return a formal string representation of the book for debugging
        return f"Book({self.title!r}, {self.author!r}, {self.year!r})"
