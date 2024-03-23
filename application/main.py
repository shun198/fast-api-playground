from fastapi import FastAPI

from routers import common, user

app = FastAPI(
    title="FastAPI Playground",
    version="0.0.1",
)
app.include_router(common.router, prefix="/api", tags=["common"])
app.include_router(user.router, prefix="/api/users", tags=["users"])
