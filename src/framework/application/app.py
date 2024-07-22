from __future__ import annotations

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from rich.console import Console
import logging

from .configs.base import Config

class SetupFramework:
    '''
    Handles the setup of the Framework services
    - database
    - cache
    - task queue
    - logging
    - etc
    '''
    def __init__(self):
        # Initialize APP_SETTINGS in the constructor
        self.APP_SETTINGS = Config.get_settings(self=Config)

    async def setup_database(self, console: Console) -> declarative_base:
        try:
            # Access the SQLITE_DATABASE_URL directly from APP_SETTINGS
            engine = create_engine(self.APP_SETTINGS.database_settings.SQLITE_DATABASE_URL)
            console.print(f"Setting up database")
            Base = declarative_base(bind=engine)
            console.print(f"Created database at {self.APP_SETTINGS.database_settings.SURREAL_DB_DATABASE}")
            return Base
        except Exception as e:
            console.print(f"Error setting up database: {str(e)}")
            logging.error(f"Error setting up database: {str(e)}")
    
    
    async def setup_caching(self, console: Console) -> None:
        console.print("Setting up caching using Redis")
        
        return None 
    async def setup_module_services(self, console: Console) -> None:
        pass
    
    async def setup_task_queue(self, console: Console) -> None:
        console.print("Setting up task queue using SAQ")
        
        return None    
    
    async def setup_logging(self, console: Console) -> None:
        # read the logging level from the settings config
        console.print("Setting up logging")
        return None
    
     