from __future__ import annotations
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from rich.console import Console
from rich.panel import Panel
import logging
from .configs.base import Config
from .cli.strings.messages.en_US import Messages
from ..application.configs.env_variables import Settings

class SetupFramework:
    def __init__(self):
        self.APP_SETTINGS = Config.get_settings(self=Config)

    async def setup_database(self, console: Console) -> declarative_base:
        try:
            database_url = self._get_database_url()
            database_type = self._get_database_type()
            console.print(Panel(f"Setting up {database_type} database", title="Database Setup"))

            engine = create_engine(database_url)
            Base = declarative_base()
            return Base
        except Exception as e:
            error_message = Messages.DATABASE_SETUP_ERROR
            console.print(Panel(error_message, title="Database Error", style="bold red"))
            logging.error(error_message)
            raise Exception(error_message)

    async def setup_caching(self, console: Console) -> None:
        console.print(Panel("Setting up caching using Redis", title="Cache Setup"))
        # Implement caching setup logic here

    async def setup_module_services(self, console: Console) -> None:
        console.print(Panel("Setting up module services", title="Module Services Setup"))
        # Implement module services setup logic here

    async def setup_task_queue(self, console: Console) -> None:
        console.print(Panel("Setting up task queue using SAQ", title="Task Queue Setup"))
        # Implement task queue setup logic here

    async def setup_logging(self, console: Console) -> None:
        console.print(Panel("Setting up logging", title="Logging Setup"))
        #logging_level 
        logging_level = Messages.Logging.INFO
        logging.basicConfig(level=logging_level)
        console.print(f"Logging level set to: {logging_level}")

    def _get_database_url(self) -> str:
        if self.APP_SETTINGS.database_settings.SQLITEDatabaseSettings.SQLITE_DATABASE_URI:
            return self.APP_SETTINGS.database_settings.SQLITEDatabaseSettings.SQLITE_DATABASE_URI
        elif self.APP_SETTINGS.database_settings.PostgresDatabaseSettings.POSTGRES_DB_URI:
            return self.APP_SETTINGS.database_settings.PostgresDatabaseSettings.POSTGRES_DB_URI
        else:
            error_message = Messages.Database.ERROR
            raise Exception(error_message)

    def _get_database_type(self) -> str:
        if self.APP_SETTINGS.database_settings.SQLITEDatabaseSettings.SQLITE_DATABASE_URI:
            return "SQLite"
        elif self.APP_SETTINGS.database_settings.PostgresDatabaseSettings.POSTGRES_DB_URI:
            return "PostgreSQL"
        else:
            error_message = Messages.Database.ERROR
            raise Exception(error_message)