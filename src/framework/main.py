from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from rich.console import Console



def main() -> None:
    
    console: Console = Console()
    console.print(f"Framework v{}", style="bold green")