import json
import os
from mmm.validators.json_validators import validate
from mmm.core.install import install_mod, install_mods
from mmm.core import init

class ModManager:
    
    def __init__(self):
        self.mods_file = "mods.json"

    def list_mods(self, installed):
        print("Listing mods...")

    def init_handler(self, default, force, loader, mc_version):
        init(default, force, loader, mc_version)

    def install_handler(self, mod_names):
        """Mod yükleme işlevi."""
        # mods.json dosyasının varlığını kontrol et
        if not os.path.exists(self.mods_file):
            print("mods.json file not found. Please run `mmm init` to create a new mods.json file.")
            return
            
        # Modları yükle
        if len(mod_names) == 0:
            print(mod_names)
            install_mods()
        else:
            for mod in mod_names:
                install_mod(mod)
