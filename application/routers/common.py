from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthCheck(BaseModel):
    status: str = "pass"


@router.get("/health", response_model=HealthCheck)
async def health_check():
    """ヘルスチェック用のAPI"""
    return {"status": "pass"}
