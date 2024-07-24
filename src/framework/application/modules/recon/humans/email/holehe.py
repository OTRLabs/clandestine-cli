from __future__ import annotations

"""
Uses the Holehe tool to analyze the target email & see what services it is registered

Reference:
https://github.com/megadose/holehe
"""



from typing import List, Dict

from rich.console import Console

import holehe



class HoleheEmailAnalyzers:
    '''
    Uses the Holehe tool to analyze the target email & see what services it is registered
    '''
    
    async def __init__(self, console: Console) -> None:
        
        self.console = console


    async def check_social_media(self, email: str, console: Console) -> None:
        """
        Check the target email for social media accounts using Holehe
        """
        self.console.print(f"Checking social media accounts for email: {email}")

    async def analyze_email(self, email: str, console: Console) -> None:
        """
        Analyze the target email using Holehe
        """
        self.console.print(f"Analyzing email: {email}")