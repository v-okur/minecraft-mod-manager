import requests

def search_mod(url):    
    response = requests.get(url)
    data = response.json()
    return data