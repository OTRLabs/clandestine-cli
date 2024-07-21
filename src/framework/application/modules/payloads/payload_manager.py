from __future__ import annotations


from pydantic import BaseModel


class Payload(BaseModel):
    """
    Represents a payload.
    """

    arch: str
    platform: str
    type: str
    cmd: str
    args: dict
    supported_formats: list
    format: str
    description: str
    rating: str
    language: str
    extension: str
    shellcode: bytes
    source: str
    