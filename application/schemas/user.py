# https://fastapi.tiangolo.com/tutorial/sql-databases/
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """システムユーザのschema定義

    Args:
        BaseModel
    """
    email: EmailStr = Field(
        examples=["example.com"],
        description="メールアドレス",
    )
    name: str = Field(
        max_length=255,
        examples=["テストユーザ01"],
        description="ユーザ名",
    )


class UserCreate(UserBase):
    password: str = Field(
        max_length=255,
        description="パスワード",
    )


class User(UserBase):
    id: int
    is_active: bool = Field(
        default=True,
        description="有効・無効化フラグ",
    )

    class Config:
        orm_mode = True
