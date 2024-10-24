import requests

def download_file(url):
    filename = url.split('/')[(-1)]
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            pass  # postinserted
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
            print(f'{filename} has been downloaded successfully.')