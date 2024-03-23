from fastapi import FastAPI
from routers import router

app = FastAPI(
    title="FastAPI Playground",
    version="0.0.1",
)
app.include_router(router.router)