from __future__ import annotations

class HelpCommand:
    '''A command that displays the help message.
    
    It accepts no arguments, and returns a string containing the available commands.
    
    '''
    def __init__(self):
        pass
        
    def execute(self) -> str:
        '''Executes the help command
        
        Returns:
            str: A string containing the available commands
        '''
        return "Available commands: help, exit, greet [name]"