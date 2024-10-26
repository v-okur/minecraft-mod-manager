import requests

from mmm.helpers import url_builder
from mmm.helpers.download import download_file
"""from mmm.data.find import find_matching"""
from mmm.data.write import add_mod_to_json
from mmm.api.search import search_mod

def single(version_id, context):
    
    url = url_builder.download(version_id) 
    response = requests.get(url)
    data = response.json()
    context.set_mod_data(data)
        
    if add_mod_to_json(data):
        download_file(context)
        
    if(len(data["dependencies"]) > 0):
        print(f"Found {len(data["dependencies"])} dependencies for {data["files"][0]["filename"]}")
        print(f"Installing dependencies...")
        for dependency in context.mod_data["dependencies"]:
            context.set_mode("id")
            context.set_project_id(dependency["project_id"])
            dep_name = search_mod(url_builder.search(context), mode=context.mode)
            single(dep_name, context)
    
    #return True