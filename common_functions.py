import os
from urllib.parse import urlparse, unquote

import requests


def get_file_extension(url):
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    return os.path.splitext(path)[1]


def download_image(url, save_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, 'wb') as f:
        f.write(response.content)
