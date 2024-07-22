
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
STANDARD_RICH_MESSAGING_CONFIG: str = f"{STANDARD_RICH_MESSAGING_COLOR}{STANDARD_RICH_MESSAGING_STYLE}"

ERROR_COLOR: str = "red"
ERROR_STYLE: str = "bold"
ERROR_CONFIG: str = f"{ERROR_COLOR} {ERROR_STYLE}"

CRITICAL_COLOR: str = "red3"
CRITICAL_STYLE: str = "bold"
CRITICAL_CONFIG: str = f"{CRITICAL_COLOR} {CRITICAL_STYLE}"

UPDATE_COLOR: str = "orchid"
UPDATE_STYLE: str = "italic"
UPDATE_CONFIG: str = f"{UPDATE_COLOR} {UPDATE_STYLE}"

WARNING_COLOR: str = "yellow"
WARNING_STYLE: str = "italic"
WARNING_CONFIG: str = f"{WARNING_COLOR} {WARNING_STYLE}"

SERVICE_FAILURE_COLOR: str = "yellow"
SERVICE_FAILURE_STYLE: str = "bold"
SERVICE_FAILURE_CONFIG: str = f"{SERVICE_FAILURE_COLOR} {SERVICE_FAILURE_STYLE}"

INFO_COLOR: str = "dark_slate_gray3"
INFO_STYLE: str = "italic"
INFO_CONFIG: str = f"{INFO_COLOR} {INFO_STYLE}"

DEBUG_COLOR: str = "dark_slate_green"
DEBUG_STYLE: str = "italic"
DEBUG_CONFIG: str = f"{DEBUG_COLOR} {DEBUG_STYLE}"

FATAL_COLOR: str = "red"
FATAL_STYLE: str = "italic bold"
FATAL_CONFIG: str = f"{FATAL_COLOR} {FATAL_STYLE}"

SUCCESS_COLOR: str = "green"
SUCCESS_STYLE: str = "bold"
SUCCESS_CONFIG: str = f"{SUCCESS_COLOR} {SUCCESS_STYLE}"

FAILURE_COLOR: str = "dark_red"
FAILURE_STYLE: str = f"bold italics"
FAILURE_CONFIG: str = f"{FAILURE_COLOR} {FAILURE_STYLE}"
