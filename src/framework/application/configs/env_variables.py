from __future__ import annotations
import os
from dotenv import load_dotenv

from uuid import UUID
load_dotenv()


class BaseSettings:
    APP_NAME: str = "Framework"
    DEBUG: bool = False
    TESTING: bool = False
    VERSION: str = "0.1.0"
    LANGUAGE: str = "en_US"
    
class SecuritySettings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret")
    SURREAL_DB_SECRET_KEY: str = os.getenv("SURREAL_DB_SECRET_KEY")
    
    # JWT
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", f"{BaseSettings.APP_NAME}_{UUID}_JWT_SECRET_KEY_{BaseSettings.VERSION}_{UUID}")
    
    
class ExternalWebUISettings:
    
    
    
    class NginxWebUISettings:
        NGINX_WEBUI_PORT: int = os.getenv("NGINX_WEBUI_PORT", 80)
        NGINX_WEBUI_HOST: str = os.getenv("NGINX_WEBUI_HOST")
    
    class TorWebUISettings:
        TOR_WEBUI_PORT: int = os.getenv("TOR_WEBUI_PORT", 8080)
        TOR_WEBUI_HOST: str = os.getenv("TOR_WEBUI_HOST")
        
            
class DatabaseSettings:
    
    # Database Connection
    SURREAL_DB_BASE_URL: str = os.getenv("SURREAL_DB_BASE_URL", "localhost")
    SURREAL_DB_DATABASE: str = os.getenv("SURREAL_DB_DATABASE", f"{BaseSettings.APP_NAME}")
    
    # Namespace
    SURREAL_DB_NAMESPACE: str = os.getenv("SURREAL_DB_NAMESPACE", "framework_namespace")
    
    SURREAL_DB_USER: str = os.getenv("SURREAL_DB_USER", "framework_operator")
    SURREAL_DB_PASSWORD: str = os.getenv("SURREAL_DB_PASSWORD")
    
    # HTTP API Access to SurrealDB
    SURREALDB_HTTP_URL: str = os.getenv("SURREALDB_HTTP_URL")
    SURREALDB_HTTP_SSL: bool = os.getenv("SURREALDB_HTTP_SSL", False)
    SURREALDB_HTTP_CERT: str = os.getenv("SURREALDB_HTTP_CERT", None)
    SURREALDB_HTTP_KEY: str = os.getenv("SURREALDB_HTTP_KEY", None)
    
    # Websocket
    SURREALDB_WS_URL: str = os.getenv("SURREALDB_WS_URL", "ws://localhost:8080")
    SURREALDB_WS_SSL: bool = os.getenv("SURREALDB_WS_SSL", False)
    SURREALDB_WS_CERT: str = os.getenv("SURREALDB_WS_CERT", None)
    SURREALDB_WS_KEY: str = os.getenv("SURREALDB_WS_KEY", None)
    
class Settings:
    
    base_settings: BaseSettings = BaseSettings()
    database_settings: DatabaseSettings = DatabaseSettings()