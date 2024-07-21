from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from rich.console import Console


from .application.configs.base import Config

from .application.cli.strings.messages.en_US import Messages

if TYPE_CHECKING:
    APP_SETTINGS: Config = Config.get_settings()


def main() -> None:
    
    console: Console = Console()
    console.print(f"{Messages.STARTED_MESSAGE}", style="bold green")
    
    ## load all the modules
    
if __name__ == "__main__":
    main()