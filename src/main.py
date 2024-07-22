from __future__ import annotations
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union
from rich.console import Console
from framework.application.configs.base import Config
from framework.application.cli.strings.messages.en_US import *
from framework.application.cli.console_manager import ConsoleManager
from framework.application import app
import asyncio
from rich.json import JSON

async def main() -> None:
    """
    The main function of the app.
    Launches the application and starts the CLI.
    """
    CURRENT_CONSOLE: Console = ConsoleManager.APPLICATION_CONSOLE
    CURRENT_CONSOLE.print(f"{WELCOME_MESSAGE}", style="bold blue")
    
    ## load the settings
    system_settings: app.SetupFramework = app.SetupFramework()
    
    CURRENT_CONSOLE.print(f"{LOADING_MESSAGE}", style="bold blue")
    await system_settings.setup_database(console=CURRENT_CONSOLE)
    CURRENT_CONSOLE.print(f"{DATABASE_LOADED_MESSAGE}")
    
    
    await system_settings.setup_caching(console=CURRENT_CONSOLE)
    CURRENT_CONSOLE.print(f"{CACHE_LOADED_MESSAGE}")
    
    await system_settings.setup_task_queue(console=CURRENT_CONSOLE)
    CURRENT_CONSOLE.print(f"{TASK_QUEUE_LOADED_MESSAGE}")
    
    await system_settings.setup_logging(console=CURRENT_CONSOLE)
    CURRENT_CONSOLE.print(f"{LOGGING_LOADED_MESSAGE}")
    
    
    
    CURRENT_CONSOLE.print(f"{STARTED_MESSAGE}")
    
    ## load all the modules

    ## Launch the REPL
    await ConsoleManager.start_repl(console=CURRENT_CONSOLE)

if __name__ == "__main__":
    asyncio.run(main())
