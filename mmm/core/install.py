import json
import sys

from ..helpers import url_builder, yes_or_no, get_input
from ..api import install
from ..api.search import search_mod
from ..data.parser import DataParser
from ..config import Defaults
from ..config import InstallContext
from ..models import Search

config = Defaults()

#TODO: facets and limit implementation
def install_mod(context: InstallContext) -> None:

    mod_name: str = context.mod_name
    
    url: str = url_builder.search(context)
    data: Search.Main = search_mod(url)
    
    context.set_search_data(Search.Main.from_dict(data))
        
    if not data or len(context.search_data.hits) == 0:
        print(f"{mod_name} not found.")
        return 
    
    
    if not context.confirm_all:
        
        dp: DataParser = DataParser(data=context.search_data)
        index = 0
        mod_count = len(context.search_data.hits)
        
        if mod_count == 1:
            print("\n---Only one mod found---")
            print(dp.to_prompt(index=index, mode="single"))
            answer = get_input().strip().lower()
            decision = yes_or_no(answer)
            
        else:
            while True:
                sys.stdout.write("\033[H\033[J")       
                print(dp.to_prompt(index=index))
                answer = get_input().strip().lower()
                decision = yes_or_no(answer, navigate=True)
                
                if decision == "prev":
                    index = (index - 1) % mod_count 
                    print(index)
                    print("\nReturning to previous mod...\n")
                elif decision == "next":
                    index = (index + 1) % mod_count 
                    print(index)
                    print("\nSkipping to next mod...\n")
                elif decision:
                    install.single(context.search_data.hits[index].latest_version, context)
                    return
                else:
                    print(f"Aborting installation of {mod_name}.")
                    return    
                
    install.single(context.search_data.hits[0].latest_version, context)
   
   
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
            

    