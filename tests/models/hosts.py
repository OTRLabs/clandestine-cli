from __future__ import annotations



from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

class Hosts(Base):
    __tablename__ = 'hosts'
    id: str = Column(Integer, primary_key=True)
    hostname: str = Column(String, unique=True)
    ip_address: str = Column(String, unique=True)
    port: str = Column(Integer)
    service: str = Column(String)
    is_active: str = Column(Boolean)
    