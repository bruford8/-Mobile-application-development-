from fastapi import HTTPException, status, Depends
from typing import Annotated

from schemas.book import Book
from .crud import get_book_by_slug

def prefetch_book(slug: str) -> Book:
    book = get_book_by_slug(slug)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with slug {slug!r} not found"
        )
    return book

BookDep = Annotated[Book, Depends(prefetch_book)]