from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()


@router.get("/health")
async def health_check():
    """ヘルスチェック用のAPI"""
    return {"status": "pass"}


app.include_router(router)
