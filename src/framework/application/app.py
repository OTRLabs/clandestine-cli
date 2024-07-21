from __future__ import annotations

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

    async def setup_database(self) -> declarative_base:
        try:
            # Access the SQLITE_DATABASE_URL directly from APP_SETTINGS
            engine = create_engine(self.APP_SETTINGS.database_settings.SQLITE_DATABASE_URL)
            Base = declarative_base(bind=engine)
            print(f"Created database at {self.APP_SETTINGS.database_settings.SQLITE_DATABASE_URL}")
            return Base
        except Exception as e:
            logging.error(f"Error setting up database: {str(e)}")
    async def setup_cache(self) -> None:
        
        pass
    
    async def setup_task_queue(self) -> None:
        pass
    
    async def setup_logging(self) -> None:
        # read the logging level from the settings config
        pass