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

    def search_handler(self, mod_name: str, mc_version: str, loader: str, project_type: str, min_downloads: int, max_downloads: int, sort: str) -> None:
        return None

    def init_handler(self, default: bool, force: bool, loader: str, mc_version: str) -> None:
        print(mc_version)
        init(default, force, loader, mc_version)

    def install_handler(self, mod_names: List[str], confirmall: bool, limit: str) -> None:
        """Mod yükleme işlevi."""

        validate(validation_type="install")
        
        version: str = minecraft_version()
        loader: str = mod_loader()        
        limit = limit
        print(limit)
        
        config.set_config(version=version, loader=loader)
            
        """ if len(mod_names) == 0:
            install_mods(confirmall) """
        
        for mod in mod_names:
                context: InstallContext = InstallContext(mod, confirm_all=confirmall, limit=limit if limit else 100)
                install_mod(context)
                
