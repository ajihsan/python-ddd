import unittest

from library_service.domains.book.model import Book
from library_service.domains.book.repository import BookRepository
from library_service.domains.loan.borrowing_service import BorrowingService
from library_service.domains.loan.repository import LoanRepository
from library_service.domains.member.model import Member
from library_service.domains.member.repository import MemberRepository


class TestBorrowingService(unittest.TestCase):
    def test_loan_book(self):
        book = Book(isbn=1, title="Book 1", author="Me")
        book_repository = BookRepository()
        book_repository.add(book=book)

        member = Member(member_id=1, name="Bambang")
        member_repository = MemberRepository()
        member_repository.add(member=member)

        loan_repository = LoanRepository()
        borrowing_service = BorrowingService(
            book_repository=book_repository, loan_repository=loan_repository
        )
        loan_book = borrowing_service.borrow_book(isbn=1, member=member)

        book_loaned = book_repository.find_by_isbn(1)
        self.assertEqual(book_loaned.available, False)
        self.assertEqual(loan_book.book, book_loaned)
        self.assertEqual(loan_book.member.member_id, 1)


if __name__ == "__main__":
    unittest.main()
