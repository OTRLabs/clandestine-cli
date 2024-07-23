from __future__ import annotations
from rich.console import Console
from ...windows.exec import WindowsCommandExecutor
import os

class AddUser(WindowsCommandExecutor):
    '''
    Extends the WindowsCommandExecutor class to implement a command responsible for adding a user to the target windows system system.
    '''
    async def __init__(self, console: Console, username: str, password: str):
        '''
        Constructor for the AddUser class.
        '''
        self.username: str = username
        self.password: str = password
        self.command: str = f"net user {self.username} {self.password} /add"
        console.print(f"Adding user: {self.username}")
        
    async def execute(self, console: Console) -> None:
        '''
        Execute the command on the Windows host. Optimize the command for stealth where possible, using progressively advanced TTPs.
        '''
        console.print(f"Adding user: {self.username}")
        
        try:
            # Execute the command using os.system
            os.system(self.command)
            console.print(f"User added successfully.")
        except Exception as e:
            # Handle any exceptions that occur during command execution
            console.print(f"Error adding user: {e}")
        
        console.print(f"User addition completed.") 