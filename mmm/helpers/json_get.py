import json
from mmm.exceptions import general as ex

def minecraft_version():
    try:
        with open("mods.json", "r") as f:
            data = json.load(f)
            return data["minecraft_version"]
    except FileNotFoundError as e:
        print(2)
    
def mod_loader():
    with open("mods.json", "r") as f:
        data = json.load(f)
        return data["mod_loader"]