from __future__ import annotations
from sqlalchemy import create_engine
from ..configs.base import Settings
from surrealdb import AsyncSurrealDB
from rich.console import Console
from typing import Any, List, Tuple
from ...application.cli.strings.messages.en_US import *
from surrealdb.http import *
from surrealdb.ws import * 
class SurrealDBManager:
    async def __init__(self, console: Console) -> None:
        self.surreal_db_connection: AsyncSurrealDB = AsyncSurrealDB(f"{Settings.database_settings.SURREAL_DB_BASE_URL}")
        self.surreal_db_connection.set_ssl(Settings.database_settings.SURREAL_DB_SSL)
        if Settings.database_settings.SURREALDB_HTTP_SSL == True:
            self.surreal_db_connection.set_cert(Settings.database_settings.SURREAL_DB_CERT)
            self.surreal_db_connection.set_key(Settings.database_settings.SURREAL_DB_KEY)
        elif Settings.database_settings.SURREALDB_HTTP_SSL == False:
            console.print(f"{SURREAL_DB_IS_NOT_USING_SSL_MESSAGE}")
            console.print(f"{SURREAL_DB_CONNECTION_NOT_USING_SSL_MESSAGE}")
        else:
            console.print(f"{SURREAL_DB_ERROR_WITH_SSL_MESSAGE}")
            console.print(f"{SURREAL_DB_CONNECTION_NOT_USING_SSL_MESSAGE}")
            

    
    class SurrealDBHTTPSessionManager:
        async def __init__(self, console: Console) -> None:
            self.surreal_db_http_connection: AsyncSurrealDB = AsyncSurrealDB(f"{Settings.database_settings.SURREALDB_HTTP_URL}")
            self.surreal_db_http_connection.set_ssl(Settings.database_settings.SURREALDB_HTTP_SSL)
            if Settings.database_settings.SURREALDB_HTTP_SSL == True:
                self.surreal_db_http_connection.set_cert(Settings.database_settings.SURREALDB_HTTP_CERT)
                self.surreal_db_http_connection.set_key(Settings.database_settings.SURREALDB_HTTP_KEY)
            elif Settings.database_settings.SURREALDB_HTTP_SSL == False:
                console.print(f"{SURREAL_DB_IS_NOT_USING_SSL_FOR_HTTP_MESSAGE}")
                console.print(f"{SURREAL_DB_HTTP_CONNECTION_NOT_USING_SSL_MESSAGE}")
            else:
                console.print(f"{SURREAL_DB_HTTP_ERROR_WITH_SSL_MESSAGE}")
                console.print(f"{SURREAL_DB_HTTP_CONNECTION_NOT_USING_SSL_MESSAGE}")
                
        async def connect_to_surreal_db_via_http(self) -> None:
            await self.surreal_db_http_connection.connect()


    class SurrealDBWSManager:
        async def __init__(self, console: Console) -> None:
            self.surreal_db_websocket_connection: AsyncSurrealDB = AsyncSurrealDB(f"{Settings.database_settings.SURREALDB_WS_URL}")    
            self.USING_SSL_FOR_SURREAL_DB_WEBSOCKET: str = self.surreal_db_websocket_connection.set_ssl(Settings.database_settings.SURREALDB_WS_SSL)
            if self.USING_SSL_FOR_SURREAL_DB_WEBSOCKET == True:
                self.surreal_db_websocket_connection.set_cert(Settings.database_settings.SURREALDB_WS_CERT)
                self.surreal_db_websocket_connection.set_key(Settings.database_settings.SURREALDB_WS_KEY)
            
            elif self.USING_SSL_FOR_SURREAL_DB_WEBSOCKET == False:
                console.print(f"{SURREAL_DB_IS_NOT_USING_SSL_FOR_WEBSOCKET_MESSAGE}")
                console.print(f"{SURREAL_DB_WEBSOCKET_CONNECTION_NOT_USING_SSL_MESSAGE}")
            
            else:
                console.print(f"{SURREAL_DB_WEBSOCKET_ERROR_WITH_SSL_MESSAGE}")
                console.print(f"{SURREAL_DB_WEBSOCKET_CONNECTION_NOT_USING_SSL_MESSAGE}")
                
        async def connect_to_surreal_db_via_websocket(self) -> None:
            await self.surreal_db_websocket_connection.connect()