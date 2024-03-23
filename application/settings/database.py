from models.user import User
from settings.environment_variables import settings
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import create_database, database_exists

connection_url = URL.create(
    drivername="postgresql",
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    database=settings.POSTGRES_NAME,
    port=settings.POSTGRES_PORT,
)


def init_db():
    """DBの初期化を行う"""
    engine = get_engine()
    if not database_exists(engine.url):
        # DBを新規作成する
        create_database(engine.url)

        # 定義されているテーブルを作成
        User.metadata.create_all(bind=engine)


def get_engine():
    """DBの接続情報を定義する

    Returns:
        create_engine: engineオブジェクト
    """
    # DBとの接続
    return create_engine(
        connection_url,
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

