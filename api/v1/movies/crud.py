
from fastapi import HTTPException, status
from typing import Dict, List, Optional

from schemas.movie import Movie, MovieCreate


class MovieStorage:

    def __init__(self):
        self._data: Dict[str, Movie] = {}

        self._data["inception"] = Movie(
            title="Inception",
            slug="inception",
            description="A mind-bending thriller about dream infiltration",
            year=2010,
            duration=148,
        )
        self._data["matrix"] = Movie(
            title="The Matrix",
            slug="matrix",
            description="A hacker discovers the shocking truth about reality",
            year=1999,
            duration=136,
        )

    def get_all(self) -> List[Movie]:
        return list(self._data.values())

    def get_by_slug(self, slug: str) -> Optional[Movie]:
        return self._data.get(slug)

    def create(self, movie_in: MovieCreate) -> Movie:
        new_movie = Movie(**movie_in.model_dump())

        if new_movie.slug in self._data:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Movie with slug '{new_movie.slug}' already exists"
            )

        self._data[new_movie.slug] = new_movie
        return new_movie


storage = MovieStorage()


def get_all_movies() -> List[Movie]:
    return storage.get_all()


def get_movie_by_slug(slug: str) -> Movie:
    movie = storage.get_by_slug(slug)
    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Movie with slug {slug!r} not found"
        )
    return movie


def create_movie(movie_in: MovieCreate) -> Movie:
    return storage.create(movie_in)