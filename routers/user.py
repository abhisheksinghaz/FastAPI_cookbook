from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sql_example.database import get_db
from sql_example.user_table import User
from models.user_model import UserBody, UserResponse


router = APIRouter()


@router.get("/")
async def read_users(user_id: int = None, db: Session = Depends(get_db)):
    if user_id is not None:
        # keeping this as to filter all in order to return a list,
        # to keep the response model of the endpoint consistent
        users = db.query(User).filter(User.id == user_id).all()
    else:
        users = db.query(User).all()
    return users


@router.post("/", response_model=UserResponse)
async def create_user(user: UserBody, db: Session = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.put("/", response_model=UserResponse)
async def update_user(user_id: int, user: UserBody, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    existing_user.name = user.name
    existing_user.email = user.email
    db.commit()
    db.refresh(existing_user)
    return existing_user


@router.delete("/")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(existing_user)
    db.commit()
    return {"detail": "User deleted successfully"}
