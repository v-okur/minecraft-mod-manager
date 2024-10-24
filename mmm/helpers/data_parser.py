import json
from colorama import Fore, init
from mmm.helpers.tools import yes_or_no

init(autoreset=True)

class DataParser:
    def __init__(self, data):
        self.data = data

    def to_json(self):
        mod_data = {
            
        }
        
    def to_prompt(self, index=0):
        display_data = {}
        display_data["project_id"] = self.data["hits"][index]["project_id"]
        display_data["title"] = self.data["hits"][index]["title"]
        display_data["author"] = self.data["hits"][index]["author"]
        display_data["description"] = self.data["hits"][index]["description"]
        display_data["downloads"] = self.data["hits"][index]["downloads"]
        
        print(f"{Fore.YELLOW}Project ID: {Fore.WHITE}{display_data['project_id']}")
        print(f"{Fore.YELLOW}Title: {Fore.WHITE}{display_data['title']}")
        print(f"{Fore.YELLOW}Author: {Fore.WHITE}{display_data['author']}")
        print(f"{Fore.YELLOW}Description: {Fore.WHITE}{display_data['description']}")
        print(f"{Fore.YELLOW}Downloads: {Fore.WHITE}{display_data['downloads']}")
        print(f"{Fore.GREEN}Is this the mod you want to install? {Fore.WHITE}")
        answer = input(f"{Fore.GREEN}[y]{Fore.WHITE}es / {Fore.RED}[n]{Fore.WHITE}o / {Fore.CYAN}[s]{Fore.WHITE}how next mod: ")
        return yes_or_no(answer, type="next")
        
        
        
    
    def to_search(self):
        search_data = {}
        
        
    
    
    