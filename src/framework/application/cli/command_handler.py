from __future__ import annotations

from typing import List
from rich.console import Console

from rich.json import JSON

from .commands.search import SearchCommand

from .strings.messages.en_US import *
from .strings.messages.str_formatting import *
from ..configs.base import Config

class CommandHandler:
    
    async def execute_command(command, console: Console) -> None:
        """
        Command processing logic used to handle any command fed to the REPL
        
        parses the command and returns the appropriate response
 
        """
        if command == "help":
            # Display the help message
            console.print(HELP_COMMAND_HANDLER_MESSAGE)
            ## return None to keep the REPL running
            return None

        elif command.startswith("use"):
            # Load a module
            console.print("Loading module: " + command[4:])
            return None
        elif command.startswith("search"):
            
            console.print("Searching for: " + command[7:])
            command = SearchCommand(command[7:])
            results = command.execute()
            console.print(JSON(results))
            
            return None 
        elif command == "exit":
            # Exit the REPL
            console.print(EXIT_COMMAND_HANDLER_MESSAGE)
            return None
        else:
            return "Unknown command"