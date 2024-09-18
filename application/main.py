from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from middlewares.logging import LoggingMiddleware
from routers import common, user
from settings.database import init_db
from settings.environment_variables import settings

init_db()

app = FastAPI(
    title="FastAPI Playground",
    version="0.0.1",
)

origins = settings.TRUSTED_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["x-csrftoken"],
)
app.add_middleware(LoggingMiddleware)
app.include_router(common.router, prefix="/api", tags=["common"])
app.include_router(user.router, prefix="/api/users", tags=["users"])
