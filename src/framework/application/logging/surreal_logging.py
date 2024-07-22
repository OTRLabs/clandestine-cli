from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union
from rich.console import Console

from ..configs.base import Config
from ..cli.strings.messages.en_US import *
from ..cli.console_manager import ConsoleManager
class SurrealDBLoggingUtil:
    '''
    Utility class for SurrealDB logging. Emulates some of the logging functionality of platforms like Open Telemetry, Sentry, etc.
    Uses the rich cli library to "pretty print" the cli output
    Uses config from an app instance.
    
    '''
    
    async def __init__(self, console: Console) -> None:
        '''
       Initialize the SurrealDBLoggingUtil class within the application. 
        '''
        console.print(f"{LOGGING_INITIALIZED_MESSAGE}", style="bold green")