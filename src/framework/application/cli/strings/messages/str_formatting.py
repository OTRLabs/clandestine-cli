
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


ERROR_ENUM_RICH_STRINGS_CONFIG: dict = {
    "error": "red bold",
    "critical": "red3 bold",
    "update": "orchid italic",
    "warning": "yellow italic",
    "service_failure": "yellow bold",
    "info": "dark_slate_gray3 italic",
    "debug": "dark_slate_green italic",
    "fatal": "red italic bold",
    "success": "green bold",
    "failure": "dark_red"
}
