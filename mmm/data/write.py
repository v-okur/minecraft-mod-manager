import json

from mmm.helpers.json_get import load_mods_json

def add_mod_to_json(new_mod):
    # Mevcut mods.json dosyasını yükleyelim
    data = load_mods_json()
    
    # Mod zaten var mı diye kontrol edelim
    for mod in data["mods"]:
        if new_mod["files"][0]["filename"] == mod["files"][0]["filename"]:
            print(f"{new_mod["files"][0]["filename"]} already exists in mods.json.")
            return False  # Zaten varsa eklemiyoruz
    
    # Modu listeye ekleyelim
    data["mods"].append(new_mod)
    
    # mods.json dosyasını güncelleyelim
    with open("mods.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print(f"{new_mod['name']} has been added to mods.json.")
    return True  # Başarıyla eklendi


