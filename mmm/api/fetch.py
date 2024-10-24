import json
from api.search import search_mod

def fetch_data(url):
        
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
            

