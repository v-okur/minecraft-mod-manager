from colorama import Fore, init

init(autoreset=True)

class DataParser:
    def __init__(self, data):
        self.data = data
        
    def to_json(self):
        return self.data

    def to_prompt(self, index=0):
        display_data = {
            "project_id": self.data["hits"][index]["project_id"],
            "title": self.data["hits"][index]["title"],
            "author": self.data["hits"][index]["author"],
            "description": self.data["hits"][index]["description"],
            "downloads": self.data["hits"][index]["downloads"],
        }

        print(f"{Fore.YELLOW}Project ID: {Fore.WHITE}{display_data['project_id']}")
        print(f"{Fore.YELLOW}Title: {Fore.WHITE}{display_data['title']}")
        print(f"{Fore.YELLOW}Author: {Fore.WHITE}{display_data['author']}")
        print(f"{Fore.YELLOW}Description: {Fore.WHITE}{display_data['description']}")
        print(f"{Fore.YELLOW}Downloads: {Fore.WHITE}{display_data['downloads']}")
        print(f"{Fore.GREEN}Is this the mod you want to install? {Fore.WHITE}")
        return f"{Fore.GREEN}[y]{Fore.WHITE}es / {Fore.RED}[n]{Fore.WHITE}o / {Fore.CYAN}[s]{Fore.WHITE}kip to next mod  / {Fore.CYAN}[p]{Fore.WHITE}rev: "

        
        
    
    
    