from pydantic import BaseModel, Field


class MovieCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    slug: str = Field(..., pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    year: int = Field(..., ge=1880, le=2100)
    director: str = Field(..., min_length=1, max_length=100)
    genre: str = Field(..., min_length=1, max_length=50)
    description: str | None = None


class Movie(MovieCreate):
    id: int = Field(..., ge=1)

    class Config:
        from_attributes = True