from fastapi import APIRouter, status

from schemas.movie import Movie, MovieCreate
from .crud import get_all_movies, create_movie
from .dependencies import MovieDep

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
)


@router.get("/", response_model=list[Movie])
def list_movies():
    return get_all_movies()


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_new_movie(movie_in: MovieCreate):
    return create_movie(movie_in)


@router.get("/{slug}", response_model=Movie)
def get_movie_detail(movie: MovieDep):
    return movie