from __future__ import annotations
from ....configs.base import Config
from ....configs.env_variables import Settings

    
# Assuming Config.get_settings is a static or class method returning an instance of Settings.
app_settings_instance = Config.get_settings(self=Config)


# Use the instance to access its attributes.
STARTING_UP_MESSAGE: str = f"Starting up Framework v{app_settings_instance.base_settings.VERSION}"
STARTED_MESSAGE: str = f"Started Framework v{app_settings_instance.base_settings.VERSION}"
WELCOME_MESSAGE: str = f"Welcome to Framework v{app_settings_instance.base_settings.VERSION}"
LOADING_MESSAGE: str = "Loading Framework services..."
DATABASE_LOADED_MESSAGE: str = "Database loaded"
CACHE_LOADED_MESSAGE: str = "Cache loaded"
TASK_QUEUE_LOADED_MESSAGE: str = "Task queue loaded"
LOGGING_LOADED_MESSAGE: str = "Logging loaded"

## REPL messages
EXIT_REPL_MESSAGE: str = "Exiting REPL, Thank you for using Framework"
SEARCHING_MODULES_MESSAGE: str = "Searching for modules..."
REPL_HELP_MESSAGE: str = f"[bold blue]Available commands:[/bold blue] [green]help[/green]\n\n[green]use [module_name][/green]\n\n[green]search[/green]" 
UNKNOWN_COMMAND_IN_REPL_MESSAGE:str = "Type 'help' for a list of commands"