# https://fastapi.tiangolo.com/tutorial/sql-databases/
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str = Field(
        max_length=254,
        examples=["example.com"],
        description="システムユーザのメールアドレス",
    )
    name: str = Field(
        max_length=255,
        examples=["テストユーザ01"],
        description="システムユーザのユーザ名",
    )


class UserCreate(UserBase):
    password: str = Field(
        max_length=255,
        description="システムユーザのパスワード",
    )


class User(UserBase):
    id: int
    is_active: bool = Field(
        default=True,
        description="有効・無効化フラグ",
    )

    class Config:
        orm_mode = True
