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

        

    async def check_social_media_services_for_target_email(self, email: str, console: Console) -> None:
        
        """
        Check the target email for social media accounts using Holehe
        """
        console.print(f"Importing holehe modules for checking social media services: {email}")
        from holehe.modules.social_media.discord import discord
        from holehe.modules.social_media.crevado import crevado
        from holehe.modules.social_media.bitmoji import bitmoji
        
        from holehe.modules.social_media.snapchat import snapchat
        from holehe.modules.social_media.pinterest import pinterest
        from holehe.modules.social_media.instagram import instagram
        from holehe.modules.social_media.parler import parler
        from holehe.modules.social_media.tellonym import tellonym
        from holehe.modules.social_media.twitter import twitter
        from holehe.modules.social_media.tumblr import tumblr
        from holehe.modules.social_media.patreon import patreon
        self.console.print(f"Checking social media accounts for email: {email}")

        self.console.print(f"Checking Discord account for email: {email}")
        discord_results: list = await discord(client=self.holehe_http_client, email=email, out=[])
        self.console.print(f"Discord results: {discord_results}")
        
        self.console.print(f"Checking Crevado account for email: {email}")
        crevado_results: list = await crevado(client=self.holehe_http_client, email=email, out=[])
        self.console.print(f"Crevado results: {crevado_results}")
        
        self.console.print(f"Checking Bitmoji account for email: {email}")
        bitmoji_results:list = await bitmoji(client=self.holehe_http_client, email=email, out=[])
        self.console.print(f"Bitmoji results: {bitmoji_results}")
        
        
        self.console.print(f"Checking Crevado account for email: {email}")
        await crevado(client=self.holehe_http_client, email=email, out=[])
        self.console.print(f"Finished checking social media accounts for email: {email}")
    
        self.console.print(f"Checking Snapchat account for email: {email}")
        await snapchat(client=self.holehe_http_client, email=email, out=[])
        self.console.print(f"Checking Pinterest account for email: {email}")
        
        self.console.print(f"Checking Instagram account for email: {email}")
        await pinterest(client=self.holehe_http_client, email=email, out=[])
        self.console.print(f"Checking Parler account for email: {email}")
        
        self.console.print(f"Checking Tellonym account for email: {email}")
        await tellonym(client=self.holehe_http_client, email=email, out=[])
        self.console.print(f"Checking Twitter account for email: {email}")
        
        self.console.print(f"Checking Tumblr account for email: {email}")
        await tumblr(client=self.holehe_http_client, email=email, out=[])
        
    async def analyze_email(self, email: str, console: Console) -> None:
        """
        Analyze the target email using Holehe
        """
        self.console.print(f"Analyzing email: {email}")