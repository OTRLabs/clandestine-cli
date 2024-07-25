from __future__ import annotations
import os
import dotenv

class DatabaseSettings:
    
    # Database Connection
    SURREAL_DB_BASE_URL: str = os.getenv("SURREAL_DB_BASE_URL", "localhost")
#    SURREAL_DB_DATABASE: str = os.getenv("SURREAL_DB_DATABASE", f"{BaseSettings.APP_NAME}")
    
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
    