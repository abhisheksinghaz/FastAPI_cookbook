from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=50)
    author: str = Field(..., min_length=1, max_length=50)
    year: int = Field("dummy year val", lt=2100, gt=1900)


class BookResponse(BaseModel):
    title: str
    author: str