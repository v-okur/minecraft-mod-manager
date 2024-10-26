from ..helpers import confirm_overwrite, initial_message, get_minecraft_version, confirm_mods_json
from ..validators import loader_val, version_val
import json

def init(default, force, loader, mc_version):
    if force:
        print('Used --force flag. Overwriting existing mods.json file')
    if not force:
        confirm = confirm_overwrite()
        if not confirm:
            print('Aborting setup. mods.json already exists.')
            exit()
    v = get_minecraft_version() or mc_version
    initial_message()
    modpack_name = input('modpack name: (default: minecraft_modpack) ') or 'minecraft_modpack'
    if v is not None:
        version = input(f'version: (default: {v}) ') or v
    else:
        version = input('version: ')
        while version == '' or not version_val(version):
            version = input('Minecraft version not found. Please enter the version (e.g., 1.20.1): ')
    mod_loader = input('mod loader: (default: fabric) ') or 'fabric'
    while not loader_val(mod_loader):
        mod_loader = input('Mod loader not found. Please enter the mod loader ([forge, fabric, neoforge]): ') or 'fabric'
    keywords = input('keywords: ').split(' ')
    if len(keywords) == 1 and keywords[0] == '':
        keywords = []
    author = input('author: ')
    json_data = {'modpack_name': modpack_name, 'minecraft_version': version, 'mod_loader': mod_loader, 'keywords': keywords, 'author': author, 'mods': []}
    is_it_ok = confirm_mods_json(json_data)
    if is_it_ok:
        with open('mods.json', 'w') as f:
            f.write(json.dumps(json_data, indent=4))
        print('Setup complete.')
    else:
        print('Setup aborted.')
        exit()