from __future__ import annotations
from ....configs.base import Config
from ....configs.env_variables import Settings
from ....configs.base import Config
from ....configs.env_variables import Settings
from rich import print

    
# Assuming Config.get_settings is a static or class method returning an instance of Settings.
app_settings_instance = Config.get_settings(self=Config)


# Use the instance to access its attributes.
STARTING_UP_MESSAGE: str = f"[bold]Starting up Framework v{app_settings_instance.base_settings.VERSION}[/bold]"
STARTED_MESSAGE: str = f"[bold]Started Framework v{app_settings_instance.base_settings.VERSION}[/bold]"
WELCOME_MESSAGE: str = f"[bold]Welcome to Framework v{app_settings_instance.base_settings.VERSION}[/bold]"
LOADING_MESSAGE: str = "[bold]Loading Framework services...[/bold]"
DATABASE_LOADED_MESSAGE: str = "[bold]Database loaded[/bold]"
CACHE_LOADED_MESSAGE: str = "[bold]Cache loaded[/bold]"
TASK_QUEUE_LOADED_MESSAGE: str = "[bold]Task queue loaded[/bold]"
LOGGING_LOADED_MESSAGE: str = "[bold]Logging loaded[/bold]"

## Console messages


## REPL Command Data
REPL_COMMANDS: List[str] = ["help", "use", "search", "exit"]

## REPL messages
EXIT_REPL_MESSAGE: str = "[bold red]Exiting REPL![/bold red]\n\nThank you for using Framework"
SEARCHING_MODULES_MESSAGE: str = "[bold blue]Searching for modules...[/bold blue]"
REPL_HELP_MESSAGE: str = f"[bold blue]Available commands:[/bold blue] [green]help[/green]\n\n[green]use [module_name][/green]\n\n[green]search[/green]" 
UNKNOWN_COMMAND_IN_REPL_MESSAGE:str = "[bold red]Unknown Command![/bold red] [blue]Type[/blue] '[green]help[/green]' [blue]for a list of commands[/blue]"
MODULE_NOT_FOUND_MESSAGE: str = "[bold red]Module not found![/bold red]"
MODULE_LOADED_MESSAGE: str = "[bold]Module loaded[/bold]"
MODULE_UNLOADED_MESSAGE: str = "[bold]Module unloaded[/bold]"
MODULE_RELOADED_MESSAGE: str = "[bold]Module reloaded[/bold]"
MODULE_USAGE_MESSAGE: str = "[bold]Usage: use [module_name][/bold]"
MODULE_ALREADY_LOADED_MESSAGE: str = "[bold]Module already loaded[/bold]"