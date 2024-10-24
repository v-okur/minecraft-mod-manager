import json
import os
import mmm.exceptions.general as ex
from mmm.validators import version_val, loader_val

def load_json(file_path="mods.json"):
    """JSON dosyasını yükler."""
    if not os.path.exists(file_path):
        raise ex.ModsJsonNotFound()
        
    with open(file_path, "r") as f:
        return json.load(f)

def validate_version(data):
    """Minecraft versiyonunun geçerli olup olmadığını kontrol eder."""
    if "minecraft_version" not in data:
        raise ex.ModsJsonCorrupted("minecraft_version key not found.")
    if not version_val(data["minecraft_version"]):
        print(f"\"minecraft_version\": \"{data['minecraft_version']}\"")
        raise ex.ModsJsonCorrupted("minecraft_version key is not valid.")

def validate_loader(data):
    """Mod loader'ın geçerli olup olmadığını kontrol eder."""
    if "mod_loader" not in data:
        raise ex.ModsJsonCorrupted("mod_loader key not found.")
    if not loader_val(data["mod_loader"]):
        print(f"\"mod_loader\": \"{data['mod_loader']}\"")
        raise ex.InvalidLoader()

def validate_mods(data):
    """Mods anahtarının varlığı ve tipini kontrol eder."""
    if "mods" not in data:
        raise ex.ModsJsonCorrupted("Mods key not found.")
    if not isinstance(data["mods"], list):
        raise ex.ModsJsonCorrupted("Mods key is not a list.")

def validate(data, validation_type):
    """Geçerli validation type'a göre doğrulamaları çalıştırır."""
    if validation_type in ["install", "update"]:
        validate_version(data)
        validate_loader(data)
        validate_mods(data)
    elif validation_type == "list":
        validate_mods(data)
    else:
        raise ValueError("Invalid validation type specified")
