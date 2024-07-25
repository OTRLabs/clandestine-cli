from __future__ import annotations
from typing import List
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from .commands.search import SearchCommand
from .strings.messages.en_US import Messages, CLI_COMMANDS_INDEX, create_command_table

class CommandHandler:
    @staticmethod
    async def execute_command(command: str, console: Console) -> None:
        """
        Command processing logic used to handle any command fed to the REPL
        Parses the command and returns the appropriate response
        """
        command = command.strip().lower()

        if command == "help":
            console.print(Panel(create_command_table(CLI_COMMANDS_INDEX), title="Available Commands"))
        elif command.startswith("use"):
            module = command[4:].strip()
            console.print(Panel(f"Loading module: {module}", title="Module Loader"))
        elif command.startswith("search"):
            keyword = command[7:].strip()
            console.print(Panel(f"Searching for: {keyword}", title="Search"))
            search_command = SearchCommand(keyword)
            results = search_command.execute()
            console.print(Panel.fit(results, title="Search Results"))
        elif command == "exit":
            console.print(Messages.General.EXITING)
            return "exit"
        else:
            console.print(Messages.REPL.UNKNOWN_COMMAND)

        return None