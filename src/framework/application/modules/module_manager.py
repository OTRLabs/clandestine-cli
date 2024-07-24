from __future__ import annotations

from ..cli.console_manager import ConsoleManager

class ModuleManager:
    
    async def __init__(self) -> None:
        """
        Initialize the ModuleManager class.
        
        """
        
        pass
    async def index_module_list(console: ConsoleManager.APPLICATION_CONSOLE) -> dict:
        """
        List all modules in the app.
        
        Returns:
            dict: A dictionary containing all the modules.
            
        """
        
        module_index: dict = {}
        
        return module_index