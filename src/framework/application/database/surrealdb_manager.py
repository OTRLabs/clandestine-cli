from __future__ import annotations
from sqlalchemy import create_engine
from ..configs.base import Settings
from surrealdb import AsyncSurrealDB


class SurrealDBHTTPSessionManager:
    async def __init__(self) -> None:
        self.surreal_db_http_connection: AsyncSurrealDB = AsyncSurrealDB(f"{Settings.database_settings.SURREALDB_HTTP_URL}")
        self.surreal_db_http_connection.set_ssl(Settings.database_settings.SURREALDB_HTTP_SSL)
        


class SurrealDBWSManager:
    async def __init__(self) -> None:
        self.surreal_db_websocket_connection: AsyncSurrealDB = AsyncSurrealDB(f"{Settings.database_settings.SURREALDB_WS_URL}")    
