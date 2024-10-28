from ..config import Defaults
from ..config import InstallContext
import json

config = Defaults()

def search(context: InstallContext):
    facets_str = json.dumps(context.to_facets())  # JSON formatında string hale getiriyoruz
    url = f'https://api.modrinth.com/v2/search?query={context.mod_name}&facets={facets_str}'
    
    
    if context.limit is not None:
        url += f'&limit={context.limit}'
        
    if context.offset is not None:
        url += f'&offset={context.offset}'
        
    if context.mode == "dependency":
        return search_with_id(context.project_id, facets_str)
    return url


def search_with_id(mod_id, facets_str):
    return f"https://api.modrinth.com/v2/search?project_id={mod_id}&facets=[{facets_str}]"
    
def download(version_id):
    return f"https://api.modrinth.com/v2/version/{version_id}"  

def search_dep(context: InstallContext):
    facets_str = json.dumps(context.to_facets())  # JSON
    
    return f"https://api.modrinth.com/v2/search?facets={facets_str}"
    
    