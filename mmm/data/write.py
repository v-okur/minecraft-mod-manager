import json


from ..helpers.json_get import load_mods_json

def add_mod_to_json(new_mod):
    data = load_mods_json()
    
    for mod in data["mods"]:
        if new_mod["files"][0]["filename"] == mod["files"][0]["filename"]:
            print(f"{new_mod["files"][0]["filename"]} already exists in mods.json.")
            return False
    
    data["mods"].append(new_mod)
    
    with open("mods.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print(f"{new_mod['name']} has been added to mods.json.")
    return True 


