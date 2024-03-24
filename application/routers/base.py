from settings.database import get_session


def get_db():
    """依存関係を作成する
    一回のリクエストで使用されるセッションインスタンスを作成し、
    リクエストが終了したらclose()する

    Yields:
        db: SQLAlchemyで生成したセッションインスタンス
    """
    try:
        db = get_session()
        yield db
    finally:
        db.close()
