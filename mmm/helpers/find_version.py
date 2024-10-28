import requests
from ..models import Search


def search_mod(url, version):
    print(url)
    response = requests.get(url)
    data: Search.Main = Search.Main.from_dict(response.json())
    
    try:
        for mod in data.hits:
            if mod:
                print(mod.categories)
    except KeyError as e:
        print(f"KeyError: {e}")
        pass

    return data


if __name__ == "__main__":
    url = f"https://api.modrinth.com/v2/search?facets=[[\"versions=1.16.5\"],[\"categories=fabric\"]]&limit=100"
    
    search_mod(url, '1.16.5')