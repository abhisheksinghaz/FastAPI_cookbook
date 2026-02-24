from fastapi import APIRouter

router = APIRouter()

@router.get("/{author_id}")
def get_author_details(author_id: int):
    return {
        "author_id": author_id,
        "name": str(author_id)*3
    }