from __future__ import annotations

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import logging


from .configs.base import Settings
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
        APP_SETTINGS: Config = Config.get_settings(self=Config)
        return None 
    
    async def setup_database(self, APP_SETTINGS) -> declarative_base:
        # check if the sqlite database exists
        # if not, create it
        
        engine = create_engine(APP_SETTINGS.base_settings.DATABASE_URL)
        Base = declarative_base(bind=engine)
        return Base
    
    async def setup_cache(self):
        pass
    
    async def setup_task_queue(self):
        pass
    
    async def setup_logging(self):
        # read the logging level from the settings config
        pass