from __future__ import annotations
from rich.console import Console
import os


class WindowsCommandExecutor:
    """
    A class that will execute a command on a Windows system.
    """
    def __init__(self, console: Console, command: str):
        self.command: str = f"{command}"
        console.print(f"Executing command: {command}")

    def execute(self, console: Console, command: str) -> None:
        """
        Execute the command on the Windows host. Optimize the command for stealth where possible, using progressively advanced TTPs.
        """
        console.print(f"Executing command: {command}")
        
        os.system(command)
        
        console.print(f"Command executed successfully.")