def search(mod_name, version, loader, author=None, min_downloads=None, limit=None):
    facets = []
    facets.append(f'"versions:{loader}"')
    facets.append(f'"categories:{version}"')
    if author:
        facets.append(f'"authors:{author}"')
    if min_downloads is not None:
        facets.append(f'"downloads>={min_downloads}"')
    facets_str = ','.join([f'[{facet}]' for facet in facets])
    url = f'https://api.modrinth.com/v2/search?query={mod_name}&facets=[{facets_str}]'
    if limit is not None:
        url += f'&limit={limit}'
    return url

def file(slug):
    url = f'https://api.modrinth.com/v2/project/{slug}/version'
    return url