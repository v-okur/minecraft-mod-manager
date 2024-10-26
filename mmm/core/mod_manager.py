from ..validators.json_validators import validate
from .install import install_mod, install_mods
from .init import init  # Adjusted import path for init
from ..config import Defaults
from ..helpers.json_get import mod_loader, minecraft_version
from ..config import InstallContext
from typing import List


config = Defaults()


class ModManager:
    

    def list_mods(self, installed: bool) -> None:
        print("Listing mods...")

    def init_handler(self, default: bool, force: bool, loader: str, mc_version: str) -> None:
        init(default, force, loader, mc_version)

    def install_handler(self, mod_names: List[str], confirmall: bool, limit: int) -> None:
        """Mod yükleme işlevi."""

        validate(validation_type="install")
        
        version: str = minecraft_version()
        loader: str = mod_loader()        
        
        config.set_config(version=version, loader=loader)
            
        """ if len(mod_names) == 0:
            install_mods(confirmall) """
        
        for mod in mod_names:
                context: InstallContext = InstallContext(mod, confirm_all=confirmall, limit=limit)
                install_mod(context)
                
