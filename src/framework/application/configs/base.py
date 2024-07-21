from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from .env_variables import Settings

class Config:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def get_settings(self) -> Settings:
        return self.settings