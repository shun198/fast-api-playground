from models.user import User
from schemas.user import UserCreate
from sqlalchemy.orm import Session


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    hashed_password = user.password + "notreallyhashed"
    db_user = User(email=user.email, name=user.name, password=hashed_password,)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()