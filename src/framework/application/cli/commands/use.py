from __future__ import annotations

from typing import List, Optional

class UserCommand:
    '''A command that searches your modules.
    
    It accepts a string as a query, which is the search term. 
    it searches the index of modules using regex + keywords to return the results that match
    
    '''
    async def __init__(self, query: str):
        self.query = query
        
    async def execute(self, query: str, comand_args: str) -> Optional[List[str]]:
        '''Executes the search command
        
        Returns:
            Optional[List[str]]: A list of search results
        '''
        if query.startswith("search"):
            return ["Searching for: " + query[7:]]
        
        return None
    
    