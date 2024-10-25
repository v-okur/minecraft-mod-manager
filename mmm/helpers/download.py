import requests

def download_file(url, filename):
    try:
        # Streaming mode ile indirme işlemi
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Herhangi bir hata durumunda exception fırlat
        
        print(f'Downloading {filename}...')
        # Dosya açma bloğu
        with open(f"{filename}", 'wb') as file:
            # İçeriği parça parça yazma
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # Boş chunk olup olmadığını kontrol edin
                    file.write(chunk)
        
        print(f'{filename} has been downloaded successfully.')
    
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
