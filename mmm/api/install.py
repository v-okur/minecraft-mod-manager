import requests

from ..helpers import url_builder
from ..helpers.download import download_file
"""from ..data.find import find_matching"""
from ..data.write import add_mod_to_json
from ..api.search import search_mod
from ..models import Project, Search
from ..config import InstallContext

def single(version_id, context: InstallContext) -> None:
    
    url: str = url_builder.download(version_id) 
    response: requests.Response = requests.get(url)
    data: Project.Main = response.json()
    
    context.set_project_data(Project.Main.from_dict(data))    
    
    #TODO: Model kullanılacak kesinkikle. işler çok daha kolaşlaşır.
        
    if add_mod_to_json(data):
        download_file(context)
        
    if(len(data["dependencies"]) > 0):
        print(f"Found {len(data["dependencies"])} dependencies for {data["files"][0]["filename"]}")
        print(f"Installing dependencies...")
        for dependency in context.mod_data["dependencies"]:
            if dependency["dependency_type"] == "required":
                
                context.set_mode("id")
                context.set_project_id(dependency["project_id"])
                
                print(f"Installing {dependency['project_id']}")
                
                dep_name = search_mod(url_builder.search(context))
                single(dep_name, context)
                
        context.set_mode(None)
    #return True