from __future__ import annotations
from ....configs.base import Config
from ....configs.env_variables import Settings
from ....configs.base import Config
from rich import print
from typing import List
from .str_formatting import *
# Assuming Config.get_settings is a static or class method returning an instance of Settings.
app_settings_instance = Config.get_settings(self=Config)

# Basic App Config

APP_NAME: str = "K8Sploit Framework"


STARTING_UP_MESSAGE: str = f"[{SUCCESS_CONFIG}]Starting up Framework v{app_settings_instance.base_settings.VERSION}[/{SUCCESS_CONFIG}]"
STARTED_MESSAGE: str = f"[{SUCCESS_CONFIG}]Started Framework v{app_settings_instance.base_settings.VERSION}[/{SUCCESS_CONFIG}]"
WELCOME_MESSAGE: str = f"[{STANDARD_RICH_MESSAGING_CONFIG}]Welcome to Framework v{app_settings_instance.base_settings.VERSION}[/{STANDARD_RICH_MESSAGING_CONFIG}]"
LOADING_MESSAGE: str = f"[{INFO_CONFIG}]Loading Framework services...[/{INFO_CONFIG}]"
DATABASE_LOADED_MESSAGE: str = f"[{INFO_CONFIG}]Database loaded[/{INFO_CONFIG}]"
CACHE_LOADED_MESSAGE: str = f"[{SUCCESS_CONFIG}]Cache loaded[/{SUCCESS_CONFIG}]"
TASK_QUEUE_LOADED_MESSAGE: str = f"[{SUCCESS_CONFIG}]Task queue loaded[/{SUCCESS_CONFIG}]"
LOGGING_LOADED_MESSAGE: str = f"[{SUCCESS_CONFIG}]Logging loaded[/{SUCCESS_CONFIG}]"

## Console messages


## REPL Command Data
REPL_COMMANDS: list[dict] = [{
    "help": {
        "name": "help",
        "description": "List available commands",
        "usage": "help"
    },
    
    "use": {
        "name": "use",
        "description": "Load a module",
        "usage": "use [module_name]"
    },
    "search": {
        "name": "search",
        "description": "Search for modules",
        "usage": "search [keyword]"
    }, 
    "exit": {
        "name": "exit",
        "description": "Exit the REPL",
        "usage": "exit"
    },
}]


## REPL STRINGS
PROMPT_MESSAGE_COLOR: str = "blue bold"
PROMPT_MESSAGE: str = f"[{PROMPT_MESSAGE_COLOR}]>>>[/{PROMPT_MESSAGE_COLOR}]"

## REPL messages
OFFER_EXIT_COMMAND_MESSAGE: str = "[bold]Type 'exit' to exit the REPL[/bold]"
EXITING_REPL_MESSAGE: str = "[bold red]Exiting REPL![/bold red]\n\nThank you for using Framework"

## Starting repl
STARTING_REPL_MESSAGE: str = f"[bold blue]Starting {APP_NAME} REPL[/bold blue]"
STARTED_REPL_MESSAGE: str = f"[bold blue]{APP_NAME} REPL started[/bold blue]"

REPL_HELP_MESSAGE: str = f"help: {REPL_COMMANDS}"


# HELP messages
SHORT_VERSION_REPL_HELP_MESSAGE: str = f"[bold blue]Available commands:[/bold blue] [green]help[/green]\n\n[green]use [module_name][/green]\n\n[green]search[/green]" 
UNKNOWN_COMMAND_IN_REPL_MESSAGE:str = "[bold red]Unknown Command![/bold red] [blue]Type[/blue] '[green]help[/green]' [blue]for a list of commands[/blue]"



## Module messages
SEARCHING_MODULES_MESSAGE: str = f"[{STANDARD_RICH_MESSAGING_CONFIG}]Searching for modules...[/{STANDARD_RICH_MESSAGING_CONFIG}]"
MODULE_NOT_FOUND_MESSAGE: str = "[bold red]Module not found![/bold red]"
MODULE_LOADED_MESSAGE: str = "[bold]Module loaded[/bold]"
MODULE_UNLOADED_MESSAGE: str = "[bold]Module unloaded[/bold]"
MODULE_RELOADED_MESSAGE: str = "[bold]Module reloaded[/bold]"
MODULE_USAGE_MESSAGE: str = "[bold]Usage: use [module_name][/bold]"
MODULE_ALREADY_LOADED_MESSAGE: str = "[bold]Module already loaded[/bold]"
OPTIONS_MESSAGE: str = "[bold]Options[/bold]"

### Social Engineering messages

#### Phishing messages
PHISHING_MODULES: str = "[bold]Phishing Modules[/bold]"



# Database messages
DATABASE_CONNECTION_SUCCESS_MESSAGE: str = "[bold]Database connection successful[/bold]"
DATABASE_CONNECTION_FAILURE_MESSAGE: str = "[bold red]Database connection failed[/bold red]"
DATABASE_CONNECTION_SUCCESS_MESSAGE: str = "[bold]Database connection successful[/bold]"

CHECKING_IF_DATABASE_EXISTS_MESSAGE: str = "[bold]Checking if database exists...[/bold]"

## SurrealDB messages websocket
LOADING_SURREALDB_WEBSOCKET_MESSAGE: str = "[bold]Loading SurrealDB Websocket...[/bold]"
SURREAL_DB_IS_NOT_USING_SSL_FOR_WEBSOCKET_MESSAGE: str = "[bold]SurrealDB is not using SSL for websocket[/bold]"
SURREAL_DB_IS_USING_SSL_FOR_WEBSOCKET_MESSAGE: str = "[bold]SurrealDB is using SSL for websocket[/bold]"
SURREAL_DB_WEBSOCKET_CONNECTION_SUCCESS_MESSAGE: str = "[bold]SurrealDB websocket connection successful[/bold]"
SURREAL_DB_WEBSOCKET_CONNECTION_USING_SSL_MESSAGE: str = "[bold]SurrealDB websocket connection using SSL[/bold]"
SURREAL_DB_WEBSOCKET_CONNECTION_NOT_USING_SSL_MESSAGE: str = "[bold]SurrealDB websocket connection not using SSL[/bold]"
SURREAL_DB_WEBSOCKET_ERROR_WITH_SSL_MESSAGE: str = "[bold red]Error with SSL[/bold red]"
## SurrealDB messages http
LOADING_SURREALDB_HTTP_MESSAGE: str = "[bold]Loading SurrealDB HTTP...[/bold]"
SURREALDB_HTTP_CONNECTION_SUCCESS_MESSAGE: str = "[bold]SurrealDB HTTP connection successful[/bold]"
SURREALDB_HTTP_CONNECTION_USING_SSL_MESSAGE: str = "[bold]SurrealDB HTTP connection using SSL[/bold]"
SURREALDB_HTTP_CONNECTION_NOT_USING_SSL_MESSAGE: str = "[bold]SurrealDB HTTP connection not using SSL[/bold]"
SURREAL_DB_HTTP_ERROR_WITH_SSL_MESSAGE: str = "[bold red]Error with SSL[/bold red]"
SURREAL_DB_IS_NOT_USING_SSL_MESSAGE: str = "[bold]SurrealDB is not using SSL[/bold]"
SURREAL_DB_IS_USING_SSL_MESSAGE: str = "[bold]SurrealDB is using SSL[/bold]"
SURREAL_DB_CONNECTION_NOT_USING_SSL_MESSAGE: str = "[bold]SurrealDB connection not using SSL[/bold]"
SURREAL_DB_ERROR_WITH_SSL_MESSAGE: str = "[bold red]Error with SSL[/bold red]"
SURREAL_DB_HTTP_CONNECTION_NOT_USING_SSL_MESSAGE: str = "[bold]SurrealDB HTTP connection not using SSL[/bold]"
SURREAL_DB_IS_NOT_USING_SSL_FOR_HTTP_MESSAGE: str = "[bold]SurrealDB is not using SSL for HTTP[/bold]"




## SurrealDB Logging Messages
LOGGING_INITIALIZED_MESSAGE: str = f"[]Logging initialized[/]"
LOGGING_ERROR_MESSAGE: str = "[bold red]Logging error[/bold red]"
LOGGING_WARNING_MESSAGE: str = "[bold yellow]Logging warning[/bold yellow]"
LOGGING_INFO_MESSAGE: str = "[bold]Logging info[/bold]"
LOGGING_DEBUG_MESSAGE: str = "[bold]Logging debug[/bold]"
LOGGING_CRITICAL_MESSAGE: str = "[bold red]Logging critical[/bold red]"
LOGGING_FATAL_MESSAGE: str = "[bold red]Logging fatal[/bold red]"
LOGGING_SUCCESS_MESSAGE: str = "[bold]Logging success[/bold]"
LOGGING_FAILURE_MESSAGE: str = "[bold red]Logging failure[/bold red]"


