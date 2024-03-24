from cruds import user
from fastapi import APIRouter, Depends, HTTPException, status
from routers.base import get_db
from schemas.user import User, UserCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("", response_model=list[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """ユーザ一覧表示用のAPI"""
    users = user.get_users(db, skip=skip, limit=limit)
    return users


@router.post("", response_model=User)
def create_user(create_user: UserCreate, db: Session = Depends(get_db)):
    db_user = user.get_user_by_email(db, email=create_user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="すでに登録されているメールアドレスです",
        )
    return user.create_user(db=db, user=create_user)
