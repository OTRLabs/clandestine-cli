from __future__ import annotations


from rich.console import Console
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from ...configs.base import Config
from ...configs.base import Settings

from ...cli.strings.messages import *

class ListenerManagers:
    class HTTPListenerManager:
        async def __init__(self, console: Console) -> None:
            self.console = console
            self.listener = None
            self.listener = await self.setup_http_listener(console=self.console)
            self.console.print(f"HTTP Listener setup complete")
    class HTTPSListenerManager:
        async def __init__(self, console: Console) -> None:
            self.console = console
            self.listener = None
            self.listener = await self.setup_https_listener(console=self.console)
            self.console.print(f"HTTPS Listener setup complete")
        
        