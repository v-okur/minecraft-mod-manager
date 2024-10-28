from colorama import Fore, init
from ..models import Search
from ..config import InstallContext
init(autoreset=True)

class DataParser:
    def __init__(self, context: InstallContext):
        self.data = context.search_data
        self.offset = context.offset
        self.limit = context.limit
        
    def to_json(self):
        return self.data
    
    def to_search(self):
        return self.data.hits

    def to_prompt(self, index=0, mode=None):
        display_data = {
            
            "project_id": self.data.hits[index].project_id,
            "title": self.data.hits[index].title,
            "author": self.data.hits[index].author,
            "description": self.data.hits[index].description,
            "downloads": self.data.hits[index].downloads,
        }
        print(f"\n{Fore.GREEN}Page:{Fore.WHITE}{int((self.offset) / (self.limit)) + 1}/{int((self.data.total_hits -1) / self.limit) + 1}")
        print(f"{Fore.GREEN}Mod:{Fore.WHITE}{index + 1 + self.offset}/{self.data.total_hits}")
        print(f"{Fore.YELLOW}Project ID: {Fore.WHITE}{display_data['project_id']}")
        print(f"{Fore.YELLOW}Title: {Fore.WHITE}{display_data['title']}")
        print(f"{Fore.YELLOW}Author: {Fore.WHITE}{display_data['author']}")
        print(f"{Fore.YELLOW}Description: {Fore.WHITE}{display_data['description']}")
        print(f"{Fore.YELLOW}Downloads: {Fore.WHITE}{display_data['downloads']}")
        print(f"{Fore.GREEN}Is this the mod you want to install? {Fore.WHITE}")
        p = f"{Fore.GREEN}[y]{Fore.WHITE}es / {Fore.RED}[n]{Fore.WHITE}o"
        if mode is not "single":
            p += f"\n{Fore.CYAN}[d] or <- {Fore.WHITE}prev / {Fore.CYAN}[c] or -> {Fore.WHITE}next"
        return p

        
        
    
    
    