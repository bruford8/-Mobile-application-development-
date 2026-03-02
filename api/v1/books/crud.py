
from fastapi import HTTPException, status
from typing import Dict, List, Optional

from schemas.book import Book, BookCreate


class BookStorage:

    def __init__(self):
        self._data: Dict[str, Book] = {}

        self._data["harry"] = Book(
            title="Harry Potter and the Philosopher's Stone",
            slug="harry",
            description="The boy who lived begins his magical journey",
            pages=309,
        )
        self._data["ring"] = Book(
            title="The Lord of the Rings: The Fellowship of the Ring",
            slug="ring",
            description="The beginning of the epic quest to destroy the One Ring",
            pages=423,
        )

    def get_all(self) -> List[Book]:
        return list(self._data.values())

    def get_by_slug(self, slug: str) -> Optional[Book]:
        return self._data.get(slug)

    def create(self, book_in: BookCreate) -> Book:
        new_book = Book(**book_in.model_dump())

        if new_book.slug in self._data:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Book with slug '{new_book.slug}' already exists"
            )

        self._data[new_book.slug] = new_book
        return new_book


storage = BookStorage()


def get_all_books() -> List[Book]:
    return storage.get_all()


def get_book_by_slug(slug: str) -> Book:
    book = storage.get_by_slug(slug)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with slug {slug!r} not found"
        )
    return book


def create_book(book_in: BookCreate) -> Book:
    return storage.create(book_in)