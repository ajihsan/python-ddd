import unittest

from library_service.domains.book.model import Book
from library_service.domains.book.repository import BookRepository


class TestBook(unittest.TestCase):
    def test_add_book(self):
        book = Book(isbn=1, title="Book 1", author="Me")
        book_repository = BookRepository()
        book_repository.add(book=book)
        book_find = book_repository.find_by_isbn(isbn=1)
        self.assertEqual(book_find, book)
        self.assertEqual(book_find.title, "Book 1")


if __name__ == "__main__":
    unittest.main()
