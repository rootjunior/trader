from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "localhost"
    port: int = "8000"
    debug: bool = True
    worcers_count: int = 1
    use_timezone: bool = True
    db_password: str = "password"
    db_user: str = "username"
    db_name: str = "dbname"
    db_host: str = "postgresql"

    @property
    def postgresql_dsn(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.db_user}:"
            f"{self.db_password}@"
            f"{self.db_host}/"
            f"{self.db_name}"
        )


settings = Settings()
