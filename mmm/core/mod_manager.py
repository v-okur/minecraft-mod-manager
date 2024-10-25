import json
import os
from mmm.validators.json_validators import validate
from mmm.core.install import install_mod, install_mods
from mmm.core import init
from mmm.config import Defaults
from mmm.helpers.json_get import mod_loader, minecraft_version
from config import ModContext


config = Defaults()


class ModManager:
    
    def __init__(self):
        self.mods_file = "mods.json"

    def list_mods(self, installed):
        print("Listing mods...")

    def init_handler(self, default, force, loader, mc_version):
        init(default, force, loader, mc_version)

    def install_handler(self, mod_names, confirmall):
        """Mod yükleme işlevi."""

        #* Validation for install command*#    
        validate(validation_type="install")
        
        mod_context = ModContext(mod_names, confirmall)
        
        version = minecraft_version()
        loader = mod_loader()
        
        config.set_config(version=version, loader=loader)
            
        if len(mod_names) == 0:
            install_mods(confirmall)
        else:
            for mod in mod_names:
                
                install_mod(mod)
