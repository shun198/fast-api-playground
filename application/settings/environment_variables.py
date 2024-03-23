from typing import Optional

from pydantic import BaseSettings


class VariableSettings(BaseSettings):
    """.envファイルの変数を取得する設定クラス"""

    POSTGRES_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    TEST_POSTGRES_NAME: Optional[str] = None
    CORS_ORIGIN: str
    SLACK_WEBHOOK_URL: str


settings = VariableSettings()