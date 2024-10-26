import requests
from ..config import InstallContext

def download_file(context: InstallContext) -> None:
    
    url = context.project_data.files[0].url
    filename = context.project_data.files[0].filename
    
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  
        
        print(f'Downloading {filename}...')
        with open(f"{filename}", 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  
                    file.write(chunk)
        
        print(f'{filename} has been downloaded successfully.')
    
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
