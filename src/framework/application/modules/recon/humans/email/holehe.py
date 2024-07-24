from __future__ import annotations

"""
Uses the Holehe tool to analyze the target email & see what services it is registered

Reference:
https://github.com/megadose/holehe
"""



from typing import List, Dict

from rich.console import Console

import holehe
import httpx



class HoleheEmailAnalyzers:
    '''
    Uses the Holehe tool to analyze the target email & see what services it is registered
    '''
    
    async def __init__(self, console: Console) -> None:
        
        self.console = console
        
        self.holehe_http_client: httpx.AsyncClient = httpx.AsyncClient()

        

    async def check_social_media(self, email: str, console: Console) -> None:
        
        """
        Check the target email for social media accounts using Holehe
        """
        console.print(f"Importing holehe modules for checking social media services: {email}")
        from holehe.modules.social_media.discord import discord
        from holehe.modules.social_media.crevado import crevado
        from holehe.modules.social_media.bitmoji import bitmoji
        
        self.console.print(f"Checking social media accounts for email: {email}")

        await discord(client=self.holehe_http_client, email=email, out=[])
        
    async def analyze_email(self, email: str, console: Console) -> None:
        """
        Analyze the target email using Holehe
        """
        self.console.print(f"Analyzing email: {email}")