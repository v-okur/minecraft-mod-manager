import json

from mmm.helpers import url_builder, tools
from mmm.api import install
from mmm.api.search import search_mod
from mmm.data.parser import DataParser
from mmm.config import Defaults

config = Defaults()

#TODO: facets and limit implementation
def install_mod(mod_name, facets=None, limit=None):
    version = config.get_version()
    loader = config.get_loader()

    url = url_builder.search(mod_name, version, loader)
    data = search_mod(url)
    
    if not data or len(data["hits"]) == 0:
        print(f"{mod_name} not found.")
        return

    dp = DataParser(data=data)
    index = 0
    mod_count = len(data["hits"])

    while True:
        print("\n")
        mod_info = dp.to_prompt(index=index)
        answer = input(f"{mod_info}").strip().lower()
        decision = tools.yes_or_no(answer, navigate=True)

        if answer == "q":
            print("Installation aborted.")
            return
        elif decision == "prev":
            index = (index - 1) % mod_count 
            print("\nReturning to previous mod...\n")
        elif decision == "skip":
            index = (index + 1) % mod_count 
            print("\nSkipping to next mod...\n")
        elif decision:
            install.single(data["hits"][index]["latest_version"])
            """ install.single(data["hits"][index]["slug"], loader, version) """
            print(f"{mod_name} has been installed successfully.")
            return
        else:
            print(f"Aborting installation of {mod_name}.")
            return
    

            

        
        
        
    
    
   
   
# Ziyanı yok kalsın    
def install_mods():
    with open("mods.json", "r") as f:
            data = json.load(f)
            if len(data["mods"]) == 0:
                print("No mods to install in mods.json.")
                exit()
            for mod in data["mods"]:
                install_mod(mod["name"])
    
    """ for i in data:
        if i["game_versions"] and i["game_versions"]:
            print(i["game_versions"]) """
            

    