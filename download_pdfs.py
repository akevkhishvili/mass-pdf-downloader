import json
import requests
import os
from tqdm import tqdm
import subprocess
import sys

def download_pdf(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024 # 1 Kibibyte
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(filename, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()
        if total_size != 0 and progress_bar.n != total_size:
            print("ERROR: Something went wrong with the download")
            return False
    except requests.RequestException as e:
        print(f"An error occurred while downloading {url}: {str(e)}")
        return False
    return True

# Get the directory where the executable is running
if getattr(sys, 'frozen', False):
    current_directory = os.path.dirname(sys.executable)
else:
    current_directory = os.path.dirname(os.path.abspath(__file__))

json_file_path = os.path.join(current_directory, 'urls.json')
with open(json_file_path, 'r') as file:
    data = json.load(file)
    urls = data['urls']

for i, url in enumerate(urls):
    print(f"Downloading {url}...")
    filename = os.path.join(current_directory, f'file{i}.pdf')
    if download_pdf(url, filename):
        print(f"Downloaded {filename} successfully!")
    else:
        print(f"Failed to download {filename}. Moving to the next file...")

print("All files downloaded successfully!")
subprocess.run(f'explorer "{current_directory}"')