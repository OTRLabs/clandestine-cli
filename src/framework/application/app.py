from __future__ import annotations

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



from .configs.base import Settings
class SetupFramework:
    '''
    Handles the setup of the Framework services
    - database
    - cache
    - task queue
    - logging
    - etc
     
    '''
    def __init__(self, app):
        # Add your code here
        pass
    
    async def setup_database(self):
        # check if the sqlite database exists
        # if not, create it
        engine = create_engine(Settings.database_settings.SQLITE_DATABASE_URL)
        Base = declarative_base(bind=engine)
        return Base