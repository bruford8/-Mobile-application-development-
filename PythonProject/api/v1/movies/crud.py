from fastapi import HTTPException, status
from typing import Dict, List

from schemas.movie import Movie, MovieCreate


class MovieStorage:
    def __init__(self):
        self._data: Dict[str, Movie] = {}
        self._next_id: int = 1
        self._seed_initial_data()

    def _seed_initial_data(self) -> None:
        initial_movies = [
            {
                "title": "Inception",
                "slug": "inception",
                "year": 2010,
                "director": "Christopher Nolan",
                "genre": "Sci-Fi",
                "description": "A thief who steals corporate secrets through dream-sharing technology",
            },
            {
                "title": "The Matrix",
                "slug": "the-matrix",
                "year": 1999,
                "director": "Lana Wachowski, Lilly Wachowski",
                "genre": "Sci-Fi",
                "description": "A computer hacker learns about the true nature of reality",
            },
        ]

        for data in initial_movies:
            movie = Movie(id=self._next_id, **data)
            self._data[movie.slug] = movie
            self._next_id += 1

    def get_all(self) -> List[Movie]:
        return list(self._data.values())

    def get_by_slug(self, slug: str) -> Movie:
        movie = self._data.get(slug)
        if movie is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Movie with slug '{slug}' not found"
            )
        return movie

    def create(self, movie_in: MovieCreate) -> Movie:
        if movie_in.slug in self._data:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Movie with slug '{movie_in.slug}' already exists"
            )

        new_movie = Movie(
            id=self._next_id,
            **movie_in.model_dump()
        )
        self._data[new_movie.slug] = new_movie
        self._next_id += 1
        return new_movie

_storage = MovieStorage()


def get_all_movies() -> List[Movie]:
    return _storage.get_all()


def get_movie_by_slug(slug: str) -> Movie:
    return _storage.get_by_slug(slug)


def create_movie(movie_in: MovieCreate) -> Movie:
    return _storage.create(movie_in)