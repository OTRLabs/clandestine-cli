from __future__ import annotations
from rich.console import Console



class NodeJsSingle:
    async def __init__(self, console: Console):
        self.console = console
        console.print("[bold green]Node.js Single Payload[/bold green]")
    async def generate(self) -> str:
        self.console.print("[bold red]Generate method not implemented[/bold red]")
        return f"""{self.__class__.__name__}"""
    
    async def execute(self):
        self.console.print("[bold red]Execute method not implemented[/bold red]")
        return f"""{self.__class__.__name__}"""