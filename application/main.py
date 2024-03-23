from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Playground",
    version="0.0.1",
)

@app.get("/api/health", tags=["health"])
async def health_check():
    return {"msg": "pass"}