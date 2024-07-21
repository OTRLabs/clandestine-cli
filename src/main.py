from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from rich.console import Console


from framework.application.configs.base import Config

from framework.application.cli.strings.messages.en_US import *
from framework.application.cli.console_manager import ConsoleManager
if TYPE_CHECKING:
    APP_SETTINGS: Config = Config.get_settings()
    CURRENT_CONSOLE: Console = ConsoleManager.APPLICATION_CONSOLE

def main() -> None:
    """
    The main function of the app.
        
    """
    
    CURRENT_CONSOLE.print(f"{WELCOME_MESSAGE}", style="bold blue")
    
    CURRENT_CONSOLE.print(f"{STARTED_MESSAGE}", style="bold green")
    
    ## load all the modules

if __name__ == "__main__":
    main()