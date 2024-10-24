import json

from mmm.helpers import json_get, url_bulder
from mmm.api import install
from mmm.api.search import search_mod
from mmm.helpers.data_parser import DataParser

#TODO: facets ve limit için de implementasyon yapılacak
def install_mod(mod_name, facets=None, limit=None):
    version = json_get.minecraft_version()
    loader = json_get.mod_loader()
#!    print(f"Installing {mod_name} for Minecraft {version} with {loader} loader.")

    url = url_bulder.search(mod_name, loader, version)
    data = search_mod(url)
    if data is None:
        print(f"{mod_name} not found.")
        
    else:
        index = 1
        
        dp = DataParser(data=data)
        decision = dp.to_prompt()
        while decision == "skip" and index < len(data["hits"]):
            print("\nSkipping to next mod...\n")
            decision = dp.to_prompt(index=index)
            index += 1
        if decision is True:
            install.single(dp.slug, version, loader)
        elif index == len(data["hits"]):
            print("Mod not found.")
        else:
            print(f"Aborting installation of {mod_name}.")
            
            
        
        
        
    
    
   
   
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
            

    