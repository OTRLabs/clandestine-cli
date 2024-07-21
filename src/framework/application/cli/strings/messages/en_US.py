from __future__ import annotations
from ....configs.base import Config
from ....configs.env_variables import Settings

    
# Assuming Config.get_settings is a static or class method returning an instance of Settings.
app_settings_instance = Config.get_settings()


# Use the instance to access its attributes.
STARTING_UP_MESSAGE: str = f"Starting up Framework v{app_settings_instance.settings.base_settings.VERSION}"
STARTED_MESSAGE: str = f"Started Framework v{app_settings_instance.settings.base_settings.VERSION}"
WELCOME_MESSAGE: str = f"Welcome to Framework v{app_settings_instance.settings.base_settings.VERSION}"