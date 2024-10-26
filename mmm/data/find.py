
#!*****************************************************************!
#!*************************     TODO      *************************!
#!*****************************************************************!


"""TODO:Search için flagler eklenecek
        ve bu find matchingi kullanmadan çözebilir miyiz ona bakacağız
"""

#python annotation are used like this

def find_matching(data: dict, loader: str, version: str) -> bool:
    for mod in data:
        if loader in mod["loaders"] and version in mod["game_versions"]:
            return mod 
    return False



