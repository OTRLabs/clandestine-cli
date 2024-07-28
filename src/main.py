from __future__ import annotations
from rich.console import Console
from rich.progress import Progress
from framework.application.configs.base import Config
from framework.application.cli.strings.messages.en_US import Messages
from framework.application.cli.console_manager import ConsoleManager
from framework.application import app
import asyncio

async def main() -> None:
    """
    The main function of the app.
    Launches the application and starts the CLI.
    """
    console: Console = ConsoleManager.APPLICATION_CONSOLE
    console.print(Messages.General.WELCOME)
    
    system_settings: app.SetupFramework = app.SetupFramework()
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Setting up...", total=5)

        console.print(Messages.General.LOADING)
        
        setup_steps: list[tuple] = [
            ("setup_database", Messages.Database.LOADED),
            ("setup_caching", Messages.General.LOADING.format(component="Cache")),
            ("setup_task_queue", Messages.General.LOADING.format(component="Task Queue")),
            ("setup_logging", Messages.Logging.INITIALIZED),
            ("setup_module_services", Messages.General.LOADING.format(component="Module Services"))
        ]

        for step, message in setup_steps:
            try:
                await getattr(system_settings, step)(console=console)
                console.print(message)
                progress.update(task, advance=1)
            except Exception as e:
                console.print(f"[bold red]Error during {step}: {str(e)}[/bold red]")
                return

    console.print(Messages.General.STARTED)
    
    await ConsoleManager.start_repl(console=console)

if __name__ == "__main__":
    asyncio.run(main())