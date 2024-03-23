from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

from settings.environment_variables import settings

DATABASE_URL = URL.create(
    drivername="postgres",
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    database=settings.POSTGRES_NAME,
    port=settings.POSTGRES_PORT,
)


def get_engine():
    """DBの接続情報を定義する

    Returns:
        create_engine: engineオブジェクト
    """
    # DBとの接続
    return create_engine(
        DATABASE_URL,
        # 文字コードを指定
        encoding="utf8mb4",
        hide_parameters=True,
    )


def get_session():
    """セッションの取得

    Returns:
        scoped_session: DBのsessionインスタンス
    """
    engine = get_engine()
    session = scoped_session(
        # ORMの設定。自動コミットと自動反映はオフにする
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    return session


Base = declarative_base()
