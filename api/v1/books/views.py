from fastapi import APIRouter

from schemas.book import Book, BookCreate
from .dependencies import BookDep
from .crud import get_all_books, create_book

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=list[Book])
def get_books():
    return get_all_books()

@router.post("/", response_model=Book, status_code=201)
def create_new_book(book_in: BookCreate):
    return create_book(book_in)

@router.get("/{slug}", response_model=Book)
def get_book_detail(book: BookDep):
    return book