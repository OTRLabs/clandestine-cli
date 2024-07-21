from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from rich.console import Console


from .application.configs.base import Config

if TYPE_CHECKING:
    APP_SETTINGS: Config = Config.get_settings()


def main() -> None:
    
    console: Console = Console()
    console.print(f"Starting up Framework v{APP_SETTINGS.settings.base_settings.VERSION}", style="bold green")
    
    
if __name__ == "__main__":
    main()