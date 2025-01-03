import requests

from ..helpers import url_builder
from ..helpers.download import download_file
from ..data.write import add_mod_to_json
from ..api.search import search_mod
from ..models import Project, Search
from ..config import InstallContext

def single(version_id, ctx: InstallContext) -> None:
    url: str = url_builder.download(version_id) 
    response: requests.Response = requests.get(url)
    data: Project.Main = response.json()
    
    ctx.set_project_data(Project.Main.from_dict(data))

    if add_mod_to_json(ctx.project_data):
        download_file(ctx)
        
    dependencies_to_install = ctx.project_data.dependencies
    while dependencies_to_install:
        current_dependencies = dependencies_to_install
        dependencies_to_install = [] 
        for dependency in current_dependencies:
            
            if dependency.dependency_type != "required":
               continue
           
            new_ctx = InstallContext(ctx.mod_name)
            new_ctx.set_version_and_loader(ctx.version, ctx.loader)
            new_ctx.set_project_id(dependency.project_id)
            
            facets_str = ','.join(new_ctx.to_facets())
            uri = url_builder.search_dep(dependency.project_id, facets_str)
            search_data = search_mod(uri)
            new_ctx.set_search_data(search_data)

            if new_ctx.search_data.hits:
                dep_version_id = new_ctx.search_data.hits[0].latest_version
                new_ctx.search_data.hits[0].slug
                print(f"Installing dependency: {new_ctx.search_data.hits[0].slug}")
                
                single(dep_version_id, new_ctx)
                
                dependencies_to_install.extend(new_ctx.project_data.dependencies)

    ctx.set_mode(None)
