# https://fastapi.tiangolo.com/tutorial/sql-databases/
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str
    name: str = Field(max_length=255)


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
