from typing import List, Optional

from schemas.movie import Movie, MovieCreate

MOVIES_DB: List[Movie] = [
    Movie(
        title="Harry Potter and the Philosopher's Stone",
        slug="harry-potter-1",
        description="The boy who lived begins his journey at Hogwarts.",
        year=2001,
        duration=152,
    ),
    Movie(
        title="The Lord of the Rings: The Fellowship of the Ring",
        slug="lotr-fellowship",
        description="A shy young hobbit and his friends set out to destroy a powerful ring.",
        year=2001,
        duration=178,
    ),
    Movie(
        title="Inception",
        slug="inception-2010",
        description="A thief who steals corporate secrets through dream-sharing technology.",
        year=2010,
        duration=148,
    ),
]


def get_all_movies() -> List[Movie]:
    return MOVIES_DB


def get_movie_by_slug(slug: str) -> Optional[Movie]:
    for movie in MOVIES_DB:
        if movie.slug == slug:
            return movie
    return None


def create_movie(movie_in: MovieCreate) -> Movie:
    new_movie = Movie(**movie_in.model_dump())
    MOVIES_DB.append(new_movie)
    return new_movie