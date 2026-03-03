from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    slug: str = Field(..., pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$", description="URL-friendly identifier")
    description: str | None = None
    pages: int = Field(..., gt=0, description="Number of pages")


class Book(BookCreate):
    id: int = Field(..., ge=1)

    class Config:
        from_attributes = True