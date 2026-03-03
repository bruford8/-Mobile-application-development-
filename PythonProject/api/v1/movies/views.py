from fastapi import APIRouter, status

from schemas.movie import Movie, MovieCreate
from .dependencies import MovieDep
from .crud import get_all_movies, create_movie

router = APIRouter(prefix="/movies", tags=["movies"])


@router.get("/", response_model=list[Movie])
def list_movies():
    """Получить список всех фильмов"""
    return get_all_movies()


@router.post("/", response_model=Movie, status_code=status.HTTP_201_CREATED)
def create_new_movie(movie_in: MovieCreate):
    """Создать новый фильм"""
    return create_movie(movie_in)


@router.get("/{slug}", response_model=Movie)
def get_movie_detail(movie: Movie = MovieDep):
    """Получить фильм по slug"""
    return movie