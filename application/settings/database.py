from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import declarative_base, sessionmaker

# connection_url = URL.create(
#     drivername="mysql",
#     username=settings.MYSQL_USER,
#     password=settings.MYSQL_PASSWORD,
#     host=settings.MYSQL_HOST,
#     database=settings.MYSQL_DATABASE,
#     port=settings.MYSQL_PORT,
#     query={"charset": "utf8mb4"},
# )
