
from __future__ import annotations
from ....configs.base import Config
from ....configs.env_variables import Settings
from ....configs.base import Config
from ....configs.env_variables import Settings
from rich import print
from typing import List
    
# Assuming Config.get_settings is a static or class method returning an instance of Settings.
app_settings_instance = Config.get_settings(self=Config)

STANDARD_RICH_MESSAGING_STYLE: str = "italic"
STANDARD_RICH_MESSAGING_COLOR: str = "blue"
# set up the configuration for the "baseline" neutral basic cli messages using BBcode
STANDARD_RICH_MESSAGING_CONFIG: str = f"{STANDARD_RICH_MESSAGING_COLOR}{STANDARD_RICH_MESSAGING_STYLE}"


ERROR_RICH_CONFIG: dict = {
    "error": "red",
    "critical": "red bold",
    "warning": "yellow",
    "service_failure": "yellow bold",
    "info": "blue",
    "debug": "green",
    "fatal": "red italic bold",
    "success": "green",
    "failure": "red"
}
