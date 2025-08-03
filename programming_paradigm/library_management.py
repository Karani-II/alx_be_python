class Book:
 def __init__(self, title , author, _is_checked_out):
    self.title = title
    self.author = author
    self._is_checked_out = _is_checked_out

class Library:
 def __init__(self):
        self._books = []
 def add_book(self, book):
        self.books.append(book)
 def check_out_book(self, book):
        if book in self.books:
            self.books.remove(book)
            book._is_checked_out = True
 def return_book(self):
        self.books.append(book)
        book._is_checked_out = False
 def list_available_books(self):
        return [book for book in self.books if not book._is_checked_out]
 

        

  
      