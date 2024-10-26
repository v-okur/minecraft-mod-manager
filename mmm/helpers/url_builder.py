from mmm.config import Defaults
from mmm.config import InstallContext

config = Defaults()

def search(context: InstallContext, id=None):
    facets_str = ','.join(context.to_facets())
    url = f'https://api.modrinth.com/v2/search?query={context.mod_name}&facets=[{facets_str}]'
    if context.limit is not None:
        url += f'&limit={context.limit}'
    if context.mode == "id":
        return search_with_id(context.project_id)
    return url

def search_with_id(mod_id):
    return f"https://api.modrinth.com/v2/search?project_id={mod_id}"
    
def download(version_id):
    return f"https://api.modrinth.com/v2/version/{version_id}"  