from __future__ import annotations

from typing import List
from rich.console import Console
from rich.prompt import Prompt
class ConsoleManager:
    APPLICATION_CONSOLE: Console = Console()
    

    def start_repl(console) -> None:
        """
        Start the Read-Eval-Print Loop
        """
        
        console.print("Starting Framework REPL", style="bold green")
        console.print("Type 'help' for a list of commands", style="bold blue")
        console.print("Type 'exit' to exit the REPL", style="bold red")
        
        
        while True:
            command: str = Prompt.ask(">>> ", style="bold blue")
            if command == "exit":
                console.print("Exiting REPL", style="bold red")
                break
            elif command == "help":
                console.print("Help is on the way", style="bold blue")
            else:
                console.print(f"Unknown command: {command}", style="bold red")