from __future__ import annotations

from typing import List, Dict

from rich.console import Console
from rich.prompt import Prompt
from ...cli.strings.messages.en_US import *
from ...cli.command_handler import CommandHandler

from rich.json import JSON



class PortScannerManagers:
    

    """
    Managers the port scanner utilities & modules.
    """

    async def __init__(self) -> None:
        """
        Initialize the ReconModuleManagers class.
        """
        self.port_scanner_index: dict = {}



    class NmapPortScannerManager:
        """
        Manages the Nmap port scanner.
        """

        async def __init__(self) -> None:
            """
            Initialize the NmapPortScannerManager class.
            """
            pass

        async def index_nmap_port_scanner_list(console: Console) -> dict:
            """
            List all nmap port scanners in the app.

            Returns:
                dict: A dictionary containing all the nmap port scanners.
            """
            nmap_port_scanner_index: dict = {}

            return nmap_port_scanner_index

    async def index_port_scanner_list(self, console: Console) -> dict:
        """
        List all port scanners in the app.

        Returns:
            dict: A dictionary containing all the port scanners.
        """
        

        return self.port_scanner_index