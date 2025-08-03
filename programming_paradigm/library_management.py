class Book:
 def __init__(self, title , author, _is_checked_out):
    self.title = title
    self.author = author
    self._is_checked_out = _is_checked_out

Class Library:
    def __init__(self):
   self.books = []
    def add_book(self, book):
        self.books.append(book)
    def check_out_book(self, book):
        if book in self.books:
            self.books.remove(book)
    def return_book(self, book):
        self.books.append(book)
    def list_available_books(self):
        return self.books

        

  
      