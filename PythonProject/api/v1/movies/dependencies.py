from fastapi import Depends

from schemas.movie import Movie
from .crud import get_movie_by_slug


def get_movie_or_404(slug: str) -> Movie:
    return get_movie_by_slug(slug)


MovieDep = Depends(get_movie_or_404)