import requests

def search_mod(url, mode=None):    
    response = requests.get(url)
    data = response.json()
    if mode == "id":
        return find_latest(data)
    return data

def find_latest(data):
    return data["hits"][0]["latest_version"]