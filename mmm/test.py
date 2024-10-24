import json
from colorama import Fore, Style, init

# Colorama'yi başlat
init(autoreset=True)

def to_prompt(data):
    display_data = {}
    display_data["project_id"] = data["hits"][0]["project_id"]
    display_data["title"] = data["hits"][0]["title"]
    display_data["author"] = data["hits"][0]["author"]
    display_data["description"] = data["hits"][0]["description"]
    display_data["downloads"] = data["hits"][0]["downloads"]

    # Renkli çıktı
    print(f"{Fore.YELLOW}Project ID: {Fore.WHITE}{display_data['project_id']}")
    print(f"{Fore.YELLOW}Title: {Fore.WHITE}{display_data['title']}")
    print(f"{Fore.YELLOW}Author: {Fore.WHITE}{display_data['author']}")
    print(f"{Fore.YELLOW}Description: {Fore.WHITE}{display_data['description']}")
    print(f"{Fore.YELLOW}Downloads: {Fore.WHITE}{display_data['downloads']}")
    print(f"{Fore.GREEN}Is this the mod you want to install? {Fore.WHITE}")
    print(f"{Fore.GREEN}[y]{Fore.WHITE}es / {Fore.RED}[n]{Fore.WHITE}o / {Fore.CYAN}[s]{Fore.WHITE}how next mod")

# json verisi
data = json.loads("""{
  "hits": [
    {
      "project_id": "8shC1gFX",
      "project_type": "mod",
      "slug": "betterf3",
      "author": "TreyRuffy",
      "title": "BetterF3",
      "description": "BetterF3 is a mod that replaces Minecraft's original debug HUD with a highly customizable, more human-readable HUD.",
      "downloads": 4560821
    }
  ],
  "offset": 0,
  "limit": 4,
  "total_hits": 22
}""")

# Fonksiyonu çağır
to_prompt(data)
