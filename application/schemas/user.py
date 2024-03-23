# https://fastapi.tiangolo.com/tutorial/sql-databases/
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    name: str = Field(max_length=255)
    is_active: bool

    class Config:
        orm_mode = True