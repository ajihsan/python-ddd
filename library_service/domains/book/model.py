class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = True

    def mark_unavailable(self):
        self.available = False

    def mark_available(self):
        self.available = True
