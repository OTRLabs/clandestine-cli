from __future__ import annotations

from typing import List
from rich.console import Console
from rich.prompt import Prompt
from .strings.messages.en_US import *
from rich import inspect
from .command_handler import CommandHandler
class ConsoleManager:
    APPLICATION_CONSOLE: Console = Console()
    

    async def start_repl(console) -> None:
        """
        Start the Read-Eval-Print Loop
        """
        
        console.print(f"Starting {APP_NAME} REPL", style="bold green")
        console.print("Type 'help' for a list of commands", style="bold blue")
        console.print("Type 'exit' to exit the REPL", style="bold red")
        
        
        while True:
            command: str = Prompt.ask("[blue bold]>>>[/blue bold] ")
            if command == "exit":
                console.print("Exiting REPL", style="bold red")
                break
            elif command.startswith("search"):
                console.print("Search is not implemented yet", style="bold blue")
            elif command == "help":
                console.print(f"{REPL_HELP_MESSAGE}:\n\nf{REPL_COMMANDS}")
            elif command == "options":
                console.print(f"{OPTIONS_MESSAGE}:\n", style="bold blue")
            else:
                console.print(f"{UNKNOWN_COMMAND_IN_REPL_MESSAGE}: {command}", style="bold red")
                
                