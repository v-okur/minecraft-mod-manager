import requests
from ..models import Search


def search_mod(url):    
    response = requests.get(url)
    
    data: Search.Main = Search.Main.from_dict(response.json())
    print(data.hits[0].project_id)

    return data
