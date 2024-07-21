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
    SQLITE_DATABASE_URL: str = os.getenv("SQLITE_DATABASE_URL", "sqlite:///./database.db")
    

class Settings:
    
    base_settings: BaseSettings = BaseSettings()
    database_settings: DatabaseSettings = DatabaseSettings()