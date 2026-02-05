from schemas.book import Book, BookCreate

BOOKS_DB = [
    Book(
        title="Harry Potter",
        slug="harry",
        description="Some description",
        pages=400,
    ),
    Book(
        title="Lord of the Rings",
        slug="ring",
        description="Some description",
        pages=800,
    ),
]


def get_all_books() -> list[Book]:
    return BOOKS_DB


def get_book_by_slug(slug: str) -> Book | None:
    return next((b for b in BOOKS_DB if b.slug == slug), None)


def create_book(book_in: BookCreate) -> Book:
    new_book = Book(**book_in.model_dump())
    BOOKS_DB.append(new_book)
    return new_book