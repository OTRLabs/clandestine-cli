from __future__ import annotations
from ....configs.base import Config
from rich.console import Console
from rich.table import Table
from rich.json import JSON
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress
from rich.progress_bar import ProgressBar
from ....configs.env_variables import Settings
from rich import print
from typing import List
from rich.repr import rich_repr
from .str_formatting import *

app_settings_instance = Config.get_settings(self=Config)

console = Console()

class Constants:
    APP_NAME = "K8Sploit Framework"
    VERSION = app_settings_instance.base_settings.VERSION

class Colors:
    STANDARD = "bold white"
    SUCCESS = "bold green"
    INFO = "bold blue"
    WARNING = "bold yellow"
    ERROR = "bold red"
    PROMPT = "blue bold"

class MessageTemplates:
    LOADING = "[{color}]Loading {component}...[/{color}]"
    LOADED = "[{color}]{component} loaded[/{color}]"
    ERROR = "[{color}]Error: {message}[/{color}]"
    COMMAND = "[{color}]{command}[/{color}]"

class Command:
    def __init__(self, name: str, slug: str, description: str, help_message: str) -> None:
        self.name = name
        self.slug = slug
        self.description = description
        self.help_message = help_message

def create_command_table(commands: List[Command]) -> Table:
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Command", style="cyan")
    table.add_column("Slug", style="green")
    table.add_column("Description", style="blue")
    table.add_column("Help", style="yellow")
    
    for command in commands:
        table.add_row(command.name, command.slug, command.description, command.help_message)
    
    return table

CLI_COMMANDS_INDEX = [
    Command("help", "help", "List available commands", "help"),
    Command("use", "use", "Load a module", "use [module_name]"),
    Command("search", "search", "Search for modules", "search [keyword]"),
    Command("exit", "exit", "Exit the REPL", "exit")
]

class Messages:
    class General:
        STARTING_UP = f"[{Colors.STANDARD}]Starting up {Constants.APP_NAME} v{Constants.VERSION}[/{Colors.STANDARD}]"
        STARTED = f"[{Colors.SUCCESS}]Started {Constants.APP_NAME} v{Constants.VERSION}[/{Colors.SUCCESS}]"
        WELCOME = f"[{Colors.STANDARD}]Welcome to {Constants.APP_NAME} v{Constants.VERSION}[/{Colors.STANDARD}]"
        LOADING = MessageTemplates.LOADING.format(color=Colors.INFO, component=f"{Constants.APP_NAME} services")
        EXITING = f"[{Colors.STANDARD}]Exiting {Constants.APP_NAME} v{Constants.VERSION}[/{Colors.STANDARD}]"

    class REPL:
        PROMPT = f"[{Colors.PROMPT}]>>>[/{Colors.PROMPT}]"
        HELP = Panel(Text("Type 'help' for a list of commands", style="italic"), title="Help")
        UNKNOWN_COMMAND = Panel(Text("Unknown command! Type 'help' for a list of commands", style=Colors.ERROR), title="Error")
        OFFER_EXIT = Text("Type 'exit' to exit the REPL", style="bold")
        EXITING = Panel(Text(f"Exiting {Constants.APP_NAME} REPL!\n\nThank you for using {Constants.APP_NAME}", style=Colors.ERROR), title="Goodbye")
        STARTING = Text(f"Starting {Constants.APP_NAME} REPL", style=Colors.INFO)
        STARTED = Text(f"{Constants.APP_NAME} REPL started", style=Colors.SUCCESS)

    class Module:
        SEARCHING = MessageTemplates.LOADING.format(color=Colors.STANDARD, component="modules")
        NOT_FOUND = Text("Module not found!", style=Colors.ERROR)
        LOADED = Text("Module loaded", style=Colors.SUCCESS)
        UNLOADED = Text("Module unloaded", style=Colors.SUCCESS)
        RELOADED = Text("Module reloaded", style=Colors.SUCCESS)
        USAGE = Text("Usage: use [module_name]", style="bold")
        ALREADY_LOADED = Text("Module already loaded", style=Colors.WARNING)
        OPTIONS = Text("Options", style="bold underline")

    class Database:
        LOADED = MessageTemplates.LOADED.format(color=Colors.SUCCESS, component="Database")
        CONNECTING = MessageTemplates.LOADING.format(color=Colors.INFO, component="Database connection")
        CONNECTION_SUCCESS = Text("Database connection successful", style=Colors.SUCCESS)
        CONNECTION_FAILURE = Text("Database connection failed", style=Colors.ERROR)
        CHECKING_EXISTS = Text("Checking if database exists...", style=Colors.INFO)
        DATABASE_EXISTS = Text("Database exists", style=Colors.SUCCESS)
        DATABASE_DOES_NOT_EXIST = Text("Database does not exist", style=Colors.ERROR)
        CREATING = MessageTemplates.LOADING.format(color=Colors.INFO, component="Database")
        CREATED = Text("Database created", style=Colors.SUCCESS)
        ERROR = Text("Database error", style=Colors.ERROR)
        WARNING = Text("Database warning", style=Colors.WARNING)
        INFO = Text("Database info", style=Colors.INFO)
        DEBUG = Text("Database debug", style=Colors.INFO)
        CRITICAL = Text("Database critical", style=Colors.ERROR)
        FATAL = Text("Database fatal", style=Colors.ERROR)
        
        class SurrealDB:
            WEBSOCKET_LOADING = MessageTemplates.LOADING.format(color=Colors.INFO, component="SurrealDB Websocket")
            HTTP_LOADING = MessageTemplates.LOADING.format(color=Colors.INFO, component="SurrealDB HTTP")
            SSL_STATUS = lambda using_ssl: Text(f"SurrealDB is {'using' if using_ssl else 'not using'} SSL", style=Colors.INFO)
            CONNECTION_SUCCESS = lambda protocol, using_ssl: Text(f"SurrealDB {protocol} connection successful" + (f" using SSL" if using_ssl else ""), style=Colors.SUCCESS)
            SSL_ERROR = Text("Error with SSL", style=Colors.ERROR)

    class Logging:
        INITIALIZED = Text("Logging initialized", style=Colors.SUCCESS)
        ERROR = Text("Logging error", style=Colors.ERROR)
        WARNING = Text("Logging warning", style=Colors.WARNING)
        INFO = Text("Logging info", style=Colors.INFO)
        DEBUG = Text("Logging debug", style=Colors.INFO)
        CRITICAL = Text("Logging critical", style=Colors.ERROR)
        FATAL = Text("Logging fatal", style=Colors.ERROR)
        SUCCESS = Text("Logging success", style=Colors.SUCCESS)
        FAILURE = Text("Logging failure", style=Colors.ERROR)

# Usage examples
AVAILABLE_COMMANDS_MESSAGE = Panel(create_command_table(CLI_COMMANDS_INDEX), title="Available Commands")
HELP_COMMAND_HANDLER_MESSAGE = Panel(create_command_table(CLI_COMMANDS_INDEX), title="Available Commands")