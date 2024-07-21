from __future__ import annotations
from ....configs.base import Config

APP_SETTINGS: Config = Config.get_settings()


class Messages:
    STARTING_UP_MESSAGE: str = f"Starting up Framework v{APP_SETTINGS.settings.base_settings.VERSION}"
    STARTED_MESSAGE: str = f"Started Framework v{APP_SETTINGS.settings.base_settings.VERSION}"
    WELCOME_MESSAGE: str = f"Welcome to Framework v{APP_SETTINGS.settings.base_settings.VERSION}"