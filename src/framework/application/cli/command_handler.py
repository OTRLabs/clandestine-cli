from __future__ import annotations

from typing import List
from rich.console import Console

from rich.json import JSON

from .commands.search import SearchCommand

from .strings.messages.en_US import *
from .strings.messages.str_formatting import *
from ..configs.base import Config
from rich.repr

@rich.repr.auto
class Command:
    '''
    Base class defining the structure for all commands
    '''
    def __init__(self, command_name: str, command_slug: str, command_description: str, help_message: str) -> None:
        self.name: str = command_name
        self.command: str = command_slug
        self.description: str = command_description
        self.help_message: str = help_message
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