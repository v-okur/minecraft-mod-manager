import json
import os
import mmm.exceptions.general as ex
from mmm.validators import version_val, loader_val

def load_json(file_path="mods.json"):
    """Loads the JSON file. Returns an empty dict if the file is empty or does not exist."""
    if not os.path.exists(file_path):
        ex.ModsJsonNotFound()
        exit()

    if os.stat(file_path).st_size == 0:
        return {}

    with open(file_path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Invalid JSON file")
            
def validate_version(data):
    """Checks if the Minecraft version is valid."""
    if "minecraft_version" not in data:
        ex.VersionKeyNotFound()
        exit()
    if not version_val(data["minecraft_version"]):
        print(f"\"minecraft_version\": \"{data['minecraft_version']}\"")
        print("Invalid version")

def validate_loader(data):
    """Checks if the mod loader is valid."""
    if "mod_loader" not in data:
        ex.ModsJsonCorrupted("mod_loader key not found.")
        exit()
    if not loader_val(data["mod_loader"]):
        print(f"\"mod_loader\": \"{data['mod_loader']}\"")
        ex.InvalidLoader()
        exit()

def validate_mods(data):
    """Checks the existence and type of the mods key."""
    if "mods" not in data:
        ex.ModsJsonCorrupted("Mods key not found.")
        exit()
    if not isinstance(data["mods"], list):
        ex.ModsJsonCorrupted("Mods key is not a list.")
        exit()

def validate(validation_type):
    data=load_json()
    """Runs validations according to the specified validation type."""
    if validation_type in ["install", "update"]:
        validate_version(data)
        validate_loader(data)
        validate_mods(data)
    elif validation_type == "list":
        validate_mods(data)
    else:
        raise ValueError("Invalid validation type specified")
