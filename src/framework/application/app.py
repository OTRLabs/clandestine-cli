from __future__ import annotations
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from rich.console import Console
from rich.panel import Panel
import logging
from .configs.base import Config
from .cli.strings.messages.en_US import Messages

class SetupFramework:
    def __init__(self):
        self.APP_SETTINGS = Config.get_settings(self=Config)

    async def setup_database(self, console: Console) -> declarative_base:
        try:
            engine = create_engine(self.APP_SETTINGS.database_settings.SQLITE_DATABASE_URL)
            Base = declarative_base(bind=engine)
            console.print(Panel(f"Created database at {self.APP_SETTINGS.database_settings.SURREAL_DB_DATABASE}", title="Database Setup"))
            return Base
        except Exception as e:
            error_message = f"Error setting up database: {str(e)}"
            console.print(Panel(error_message, title="Database Error", style="bold red"))
            logging.error(error_message)
            raise

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
        logging_level = self.APP_SETTINGS.logging_settings.LOGGING_LEVEL
        logging.basicConfig(level=logging_level)
        console.print(f"Logging level set to: {logging_level}")
     