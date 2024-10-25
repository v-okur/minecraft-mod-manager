from mmm.config import Defaults

config = Defaults()

def search(mod_name, version=None, loader=None, author=None, min_downloads=None, limit=None, mode=None):
    if version is None:
        version = config.get_version()
    
    if loader is None:
        loader = config.get_loader()

    facets = []
    facets.append(f'"versions:{version}"')
    facets.append(f'"categories:{loader}"')
    if author:
        facets.append(f'"authors:{author}"')
    if min_downloads is not None:
        facets.append(f'"downloads>={min_downloads}"')
    facets_str = ','.join([f'[{facet}]' for facet in facets])
    url = f'https://api.modrinth.com/v2/search?query={mod_name}&facets=[{facets_str}]'
    if limit is not None:
        url += f'&limit={limit}'
    if mode == "id":
        return search_with_id(mod_name)
    return url

def search_with_id(mod_id):
    return f"https://api.modrinth.com/v2/search?project_id={mod_id}"
    

""" def download(slug):
    url = f'https://api.modrinth.com/v2/project/{slug}/version'
    return url """
    
def download(version_id):
    return f"https://api.modrinth.com/v2/version/{version_id}"