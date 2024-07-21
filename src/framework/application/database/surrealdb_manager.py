from __future__ import annotations
from sqlalchemy import create_engine
from ..configs.base import Settings
from surrealdb import AsyncSurrealDB


class SurrealDBSessionManager:
    async def __init__(self) -> None:
        self.db: AsyncSurrealDB = AsyncSurrealDB(f"{Settings.database_settings}")