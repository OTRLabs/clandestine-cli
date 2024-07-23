from __future__ import annotations

from rich.console import Console



class ShellBindTcp(NodeJsSingle):
    def __init__(self, port: int):
        super().__init__()
        self.port = port

    def generate(self) -> str:
        return f"""