from __future__ import annotations

from typing import List
from rich.console import Console

from rich.json import JSON

from .commands.search import SearchCommand

class CommandHandler:
    
    async def execute_command(command, console: Console) -> None:
        """
        Command processing logic used to handle any command fed to the REPL
        
        parses the command and returns the appropriate response
        
        """
        if command == "help":
            return "Available commands: help, exit, greet [name]"
        elif command.startswith("search"):
            
            console.print("Searching for: " + command[7:])
            command = SearchCommand(command[7:])
            results = command.execute()
            console.print(JSON(results))
            
            return None 
        elif command == "exit":
            return None
        else:
            return "Unknown command"