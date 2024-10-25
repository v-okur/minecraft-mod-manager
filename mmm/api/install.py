import requests

from mmm.helpers import url_builder
from mmm.helpers.download import download_file
"""from mmm.data.find import find_matching"""
from mmm.data.write import add_mod_to_json
from mmm.api.search import search_mod

def single(version_id):
    
    url = url_builder.download(version_id) 
    response = requests.get(url)
    data = response.json()
    
    """  matching_mod = find_matching(data, loader, version) 
    print(matching_mod["files"][0]["filename"])"""
    
    if add_mod_to_json(data):
        download_file(data["files"][0]["url"], data["files"][0]["filename"])
        
    
    if(len(data["dependencies"]) > 0):
        print(f"Found {len(data["dependencies"])} dependencies for {data["files"][0]["filename"]}")
        print(f"Installing dependencies...")
        for dependency in data["dependencies"]:
            dep_name = search_mod(url_builder.search(dependency["project_id"], mode="id"), mode="id")
            single(dep_name)
    
    #return True