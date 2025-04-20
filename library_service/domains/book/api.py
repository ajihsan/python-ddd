from fastapi import APIRouter

from .model import Book
from .repository import BookRepository

router = APIRouter(prefix="/book", tags=["Book"])


@router.post("/")
def create_book(book: Book):
    BookRepository.add(book=book)


@router.get("/")
def get_book(isbn: Book.isbn):
    return BookRepository.find_by_isbn(isbn=isbn)
