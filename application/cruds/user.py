from passlib.context import CryptContext
from sqlalchemy.orm import Session

from models.user import User
from schemas.user import UserCreate, UserBase


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = user.password + "notreallyhashed"
    db_user = User(
        email=user.email,
        name=user.name,
        password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: str):
    try:
        return db.query(User).get(int(user_id))
    except Exception:
        return None


def toggle_user_active(db: Session, user: User):
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    db.commit()
    return user


def update_user(db: Session, db_user: UserBase):
    db.commit()
    return db_user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)


# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user
