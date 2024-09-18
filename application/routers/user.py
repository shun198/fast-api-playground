from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from cruds import user
from routers.base import get_db
from schemas.user import IsActiveUser, User, UserCreate

router = APIRouter()


@router.get("", response_model=list[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """ユーザ一覧表示用のAPI"""
    users = user.get_users(db, skip=skip, limit=limit)
    return users


@router.post("/invite_user", response_model=User)
def create_user(create_user: UserCreate, db: Session = Depends(get_db)):
    db_user = user.get_user_by_email(db, email=create_user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="すでに登録されているメールアドレスです",
        )
    return user.create_user(db=db, user=create_user)


@router.post("/toggle_user_active/{user_id}", response_model=IsActiveUser)
def toggle_user_active(user_id: str, db: Session = Depends(get_db)):
    db_user = user.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="存在しないユーザです",
        )
    active_user = user.toggle_user_active(db, db_user)
    return {"is_active": active_user.is_active}
