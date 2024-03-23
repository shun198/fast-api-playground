from fastapi import APIRouter

router = APIRouter()

@router.get("")
async def list_user():
    """ユーザ一覧表示用のAPI"""
    return {"status": "pass"}