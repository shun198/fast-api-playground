from fastapi import APIRouter

router = APIRouter()

@router.get("/api/health", tags=["health"])
async def health_check():
    """ヘルスチェック用のAPI"""
    return {"status": "pass"}