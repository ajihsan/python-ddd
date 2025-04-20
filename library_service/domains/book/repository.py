class BookRepository:
    def __init__(self):
        self.books = {}

    def add(self, book):
        self.books[book.isbn] = book

    def find_by_isbn(self, isbn):
        return self.books.get(isbn)
