from settings.environment_variables import settings
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = URL.create(
    drivername="postgres",
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    database=settings.POSTGRES_NAME,
    port=settings.POSTGRES_PORT,
)

engine = create_engine(DATABASE_URL)

# DBのセッションを作成
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
