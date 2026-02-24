from fastapi import APIRouter
from models import book_model

router = APIRouter()


@router.post("/")
async def create_book(book: book_model.Book):
    return book


@router.get("/")
async def read_books(year: int):
    if year:
        return {
            "year": year,
            "books": ['b1', 'b2']
        }
    return {"books": "All books"}


@router.get("/allbooks", response_model=list[book_model.BookResponse])
async def read_all_books():
    return [
        {
            "title": "T1",
            "author": "A1",
            "id": 123
        },
        {
            "title": "T2",
            "author": "A212",
            "id": 1234,
            "pages": 300
        }
    ]


@router.get("/{book_id}")
def get_book_details(book_id: int):
    return {
        "book_id": book_id,
        "desc": "I am the description of book with id: {}".format(book_id)
    }
