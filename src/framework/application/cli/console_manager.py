from __future__ import annotations

from typing import List, Dict
from rich.console import Console
from rich.prompt import Prompt
from .strings.messages.en_US import *
from .command_handler import CommandHandler
from rich.json import JSON


class ConsoleManager:
    APPLICATION_CONSOLE: Console = Console()

    async def start_repl(console: Console) -> None:
        """
        Start the Read-Eval-Print Loop
        """
        console.print(f"{STARTING_REPL_MESSAGE}")
        console.print(f"{SHORT_VERSION_REPL_HELP_MESSAGE}")
        console.print(f"{OFFER_EXIT_COMMAND_MESSAGE}")

        while True:
            command: str = Prompt.ask(PROMPT_MESSAGE)
            if command == "exit":
                console.print(EXITING_REPL_MESSAGE)
                break
            elif command.startswith("search"):
                console.print("Search is not implemented yet")
            elif command == "help":
                commands = await CommandHandler.execute_command("help", console)
                if isinstance(commands, dict):
                    console.print_json(data=commands)
                else:
                    console.print(f"{commands}")
            elif command == "options":
                console.print(f"{OPTIONS_MESSAGE}:\n")
            else:
                console.print(f"{UNKNOWN_COMMAND_IN_REPL_MESSAGE}: {command}")
