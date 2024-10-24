
import mmm.helpers.tools as tools
import mmm.helpers.download as download
import requests
from mmm.config import Color
import json

def fetch_mod_data(mod_name, loader, version, api="modrinth"):
    
    url = f"https://api.modrinth.com/v2/search?query={mod_name}&facets=[[\"versions:{version}\"],[\"categories:{loader}\"]]"
    
    data = search_mod(url)
    if(len(data) == 0):
        print("Mod not found.")
    
    else:
        
        with open("mod_data_temp.json", "w") as f:
            f.write(json.dumps(data, indent=4))
        
        print(f"{Color.YELLOW}{data['hits'][0]['title']} by {data['hits'][0]['author']}{Color.RESET}")
        print(f"{Color.CYAN}Description:{Color.RESET} {data['hits'][0]['description']}")
        print(f"{Color.GREEN}Downloads: {Color.RESET}{data['hits'][0]['downloads']}{Color.RESET}")
        answer = tools.yes_or_no(input("Is this the mod you want to install? (y/n): "))
        
        if(answer):
            print("Downloading mod...")
            download_mod(data["hits"][0]["slug"], version, loader)
        else:
            print("Aborting installation.")
            
def search_mod(url):
    response = requests.get(url)
    data = response.json()
    return data

def download_mod(slug, version, loader):
    url = f"https://api.modrinth.com/v2/project/{slug}/version"
    response = requests.get(url)
    data = response.json()
    
    for i in data:
        mod_data = i["game_versions"]
        versions = [v for v in mod_data if v == version]
        loader_data = i["loaders"]
        loaders = [l for l in loader_data if loader in l]
        if len(versions) > 0 and len(loaders) > 0:
            foundmod = i
            break
    
    file = foundmod["files"][0]["url"]
    download.download_file(file)
