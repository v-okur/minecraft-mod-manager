def find_matching(data, loader, version):
    for mod in data:
        if loader in mod["loaders"] and version in mod["game_versions"]:
            return mod 
    return False 

    