from __future__ import annotations
import os
from dotenv import load_dotenv


load_dotenv()


class BaseSettings:
    APP_NAME: str = "Framework"
    DEBUG: bool = False
    TESTING: bool = False
    VERSION: str = "0.1.0"
    LANGUAGE: str = "en_US"
class SecuritySettings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret")

class DatabaseSettings:
    SURREALDB_HTTP_URL: str = os.getenv("SURREALDB_HTTP_URL", "http://localhost:8080")
    SURREALDB_WS_URL: str = os.getenv("SURREALDB_WS_URL", "ws://localhost:8080")

class Settings:
    
    base_settings: BaseSettings = BaseSettings()
    database_settings: DatabaseSettings = DatabaseSettings()