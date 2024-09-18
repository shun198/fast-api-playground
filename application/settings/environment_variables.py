from pydantic import BaseSettings


class VariableSettings(BaseSettings):
    """.envファイルの変数を取得する設定クラス"""

    POSTGRES_NAME: str = "postgres"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432
    TRUSTED_ORIGINS: list[str] = ["localhost"]
    SLACK_WEBHOOK_URL: str = ""
    SECRET_KEY: str = "secret_key"


settings = VariableSettings()
