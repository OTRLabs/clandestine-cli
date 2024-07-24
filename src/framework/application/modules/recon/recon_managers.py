from __future__ import annotations

from typing import List, Dict

from rich.console import Console
from rich.prompt import Prompt
from ...cli.strings.messages.en_US import *
from ...cli.command_handler import CommandHandler

from rich.json import JSON



class ReconModuleManagers:

    """
    Managers the recon modules.
    """

    async def __init__(self) -> None:
        """
        Initialize the ReconModuleManagers class.
        """
        pass

    async def index_recon_module_list(console: Console) -> dict:
        """
        List all recon modules in the app.

        Returns:
            dict: A dictionary containing all the recon modules.
        """
        recon_module_index: dict = {}

        return recon_module_index