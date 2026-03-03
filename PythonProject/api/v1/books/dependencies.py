from fastapi import Depends

from schemas.book import Book
from .crud import get_book_by_slug


def get_book_or_404(slug: str) -> Book:
    return get_book_by_slug(slug)


BookDep = Depends(get_book_or_404)