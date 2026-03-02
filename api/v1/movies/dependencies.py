from fastapi import Depends, HTTPException, status
from typing import Annotated

from schemas.movie import Movie
from .crud import get_movie_by_slug


def get_movie_or_404(slug: str) -> Movie:
    movie = get_movie_by_slug(slug)
    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Movie with slug '{slug}' not found"
        )
    return movie


MovieDep = Annotated[Movie, Depends(get_movie_or_404)]