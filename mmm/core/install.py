import json

from ..helpers import url_builder, yes_or_no, get_input, clear_screen
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
    context.set_search_data(data)
    

    if not data or context.search_data.total_hits == 0:
        print(f"{mod_name} not found.")
        return 

    if not context.confirm_all:
        dp: DataParser = DataParser(context)
        context.index = 0
        mod_count = len(context.search_data.hits)
        total_mods = context.search_data.total_hits
        print(f"{total_mods} mods found.")

        if mod_count == 1:
            print("\n---Only one mod found---")
            print(dp.to_prompt(index=context.index, mode="single"))
            answer = get_input().strip().lower()
            decision = yes_or_no(answer)
        else:
            while True:
                print("\033c", end="")
                print(dp.to_prompt(index=context.index))
                answer = get_input().strip().lower()
                decision = yes_or_no(answer, navigate=True)
                
                if(context.index == 0 and decision == "prev"):
                        print("\nYou are at the beginning of the list.")
                if(context.index == mod_count - 1 and decision == "next" ): # extra check
                        print("\nYou are at the end of the list.")

                if decision == "prev":
                    if context.index > 0:
                        context.index -= 1
                    elif context.offset > 0:
                        context.offset -= int(context.limit)
                        context.search_data = search_mod(url_builder.search(context))
                        dp = DataParser(context=context)
                        context.index = int(context.limit) - 1
                        print("\n--- Moving to previous page ---\n")
                    else:
                        continue

                elif decision == "next":
                    if context.index < mod_count - 1:
                        context.index += 1
                    elif context.index == mod_count - 1 and (context.offset + mod_count) < total_mods:
                        context.offset += int(context.limit)
                        context.search_data = search_mod(url_builder.search(context))
                        dp = DataParser(context=context)
                        context.index = 0
                        print("\n--- Moving to next page ---\n")
                    else:
                        continue

                elif decision:
                    install.single(context.search_data.hits[context.index].latest_version, context)
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
            

    