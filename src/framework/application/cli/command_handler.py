from __future__ import annotations

from typing import List
from rich.console import Console



class CommandHandler:
    
    async def execute_command(command, console) -> None:
        """
        Dummy function to simulate command execution.
        In a real application, this would contain logic to process the command.
        """
        if command == "help":
            return "Available commands: help, exit, greet [name]"
        elif command.startswith("greet"):
            _, name = command.split()
            return f"Hello, {name}!"
        elif command == "exit":
            return None
        else:
            return "Unknown command"