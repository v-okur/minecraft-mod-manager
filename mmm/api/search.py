import requests

def search_mod(url):    
    response = requests.get(url)
    print(url)
    data = response.json()
    return data
