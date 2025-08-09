class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        self.title = title
        self.author = author
        self.file_size = file_size 
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        self.title = title 
        self.author = author 
        self.page_count = page_count
class Library:
    def __init__(self, books):
       self.books = []
    def add_books(self, books):
        self.books.append(books):
    def list_books(self):
        return f"{[book.title for book in self.books]}"
    

            

    

