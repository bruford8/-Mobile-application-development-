from fastapi import HTTPException, status
from typing import Dict, List

from schemas.book import Book, BookCreate


class BookStorage:
    def __init__(self):
        self._data: Dict[str, Book] = {}
        self._next_id: int = 1
        self._seed_initial_data()

    def _seed_initial_data(self) -> None:
        initial_books = [
            {
                "title": "Harry Potter and the Philosopher's Stone",
                "slug": "harry",
                "description": "The boy who lived begins his magical journey",
                "pages": 309,
            },
            {
                "title": "The Lord of the Rings: The Fellowship of the Ring",
                "slug": "ring",
                "description": "The beginning of the epic quest to destroy the One Ring",
                "pages": 423,
            },
        ]

        for data in initial_books:
            book = Book(id=self._next_id, **data)
            self._data[book.slug] = book
            self._next_id += 1

    def get_all(self) -> List[Book]:
        return list(self._data.values())

    def get_by_slug(self, slug: str) -> Book:
        book = self._data.get(slug)
        if book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with slug '{slug}' not found"
            )
        return book

    def create(self, book_in: BookCreate) -> Book:
        if book_in.slug in self._data:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Book with slug '{book_in.slug}' already exists"
            )

        new_book = Book(
            id=self._next_id,
            **book_in.model_dump()
        )
        self._data[new_book.slug] = new_book
        self._next_id += 1
        return new_book

_storage = BookStorage()

def get_all_books() -> List[Book]:
    return _storage.get_all()


def get_book_by_slug(slug: str) -> Book:
    return _storage.get_by_slug(slug)


def create_book(book_in: BookCreate) -> Book:
    return _storage.create(book_in)