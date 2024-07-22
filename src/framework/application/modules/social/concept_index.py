from __future__ import annotations

import jinja2
from rich.console import Console
from ...cli.strings.messages.en_US import * 
class SocialEngineeringModules:
    
    class PhishingModules:
        async def __init__(self, console: Console):
            self.console = console
            self.console.print(PHISHING_MODULES)
            self.console.print(PhishingModulesOptions)
            self.console.print()