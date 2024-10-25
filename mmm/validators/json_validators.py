import json
import os
import mmm.exceptions.general as ex
from mmm.validators import version_val, loader_val

def load_json(file_path="mods.json"):
    """JSON dosyasını yükler. Dosya boşsa veya mevcut değilse boş bir dict döner."""
    if not os.path.exists(file_path):
        ex.ModsJsonNotFound()
        exit()

    # Dosyanın boş olup olmadığını kontrol et
    if os.stat(file_path).st_size == 0:
        return {}

    with open(file_path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # Dosya geçerli bir JSON değilse veya boşsa boş bir dict döndür
            print("Invalid JSON file")
            
def validate_version(data):
    """Minecraft versiyonunun geçerli olup olmadığını kontrol eder."""
    if "minecraft_version" not in data:
        ex.VersionKeyNotFound()
        exit()
    if not version_val(data["minecraft_version"]):
        print(f"\"minecraft_version\": \"{data['minecraft_version']}\"")
        print("Invalid version")

def validate_loader(data):
    """Mod loader'ın geçerli olup olmadığını kontrol eder."""
    if "mod_loader" not in data:
        ex.ModsJsonCorrupted("mod_loader key not found.")
        exit()
    if not loader_val(data["mod_loader"]):
        print(f"\"mod_loader\": \"{data['mod_loader']}\"")
        ex.InvalidLoader()
        exit()

def validate_mods(data):
    """Mods anahtarının varlığı ve tipini kontrol eder."""
    if "mods" not in data:
        ex.ModsJsonCorrupted("Mods key not found.")
        exit()
    if not isinstance(data["mods"], list):
        ex.ModsJsonCorrupted("Mods key is not a list.")
        exit()

def validate(validation_type):
    data=load_json()
    """Geçerli validation type'a göre doğrulamaları çalıştırır."""
    if validation_type in ["install", "update"]:
        validate_version(data)
        validate_loader(data)
        validate_mods(data)
    elif validation_type == "list":
        validate_mods(data)
    else:
        raise ValueError("Invalid validation type specified")
