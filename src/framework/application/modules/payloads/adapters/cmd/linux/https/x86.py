from __future__ import annotations
from pydantic import BaseModel
from .....payload_manager import Payload

class X86LinuxHttpsCmdPayload(Payload, BaseModel):
    """
    Represents a payload for executing commands over HTTPS on Linux x86.
    """

    def __init__(self, **kwargs):
        """
        Initializes the X86LinuxHttpsCmdPayload object.

        Args:
            **kwargs: Additional keyword arguments.
        """
        super().__init__(**kwargs)

        # Set payload properties
        self.arch = "x86"
        self.platform = "linux"
        self.type = "https"
        self.cmd = "cmd"

        self.args = {
            "CMD": {
                "description": "Command to execute",
                "required": True,
            },
        }

        self.supported_formats = ["raw", "c", "exe", "dll", "ps1", "py", "sh"]
        self.format = "raw"
        self.description = "Command execution over HTTPS payload for Linux x86"
        self.rating = "Excellent"
        self.language = "python"
        self.extension = "py"

        # Shellcode for executing the command
        self.shellcode = (
            b"placeholer. implement function to generate shellcode on your machine"
        )

        self.source = ""
