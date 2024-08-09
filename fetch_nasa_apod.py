import os

import requests
from dotenv import load_dotenv

from common_functions import get_file_extension, download_image


def get_nasa_apod(api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': api_key, 'count': 20}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return [item['url'] for item in data]


def fetch_nasa_apod():
    load_dotenv()
    api_token_nasa = os.environ.get('API_TOKEN_NASA')

    if not api_token_nasa:
        print("API_TOKEN_NASA не найден в переменных окружения.")
        return

    try:
        image_urls = get_nasa_apod(api_token_nasa)
        print(f"Ссылки на фото дня NASA: {image_urls}")

        folder_name = 'photo_of_the_day'
        os.makedirs(folder_name, exist_ok=True)

        for i, url in enumerate(image_urls):
            file_extension = get_file_extension(url)
            file_path = os.path.join(folder_name, f"{i + 1}{file_extension}")
            download_image(url, file_path)
        print(f'Фото дня NASA сохранены в папке: {folder_name}')
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
    except FileNotFoundError as e:
        print(f"Ошибка при сохранении файла: {e}")


if __name__ == '__main__':
    fetch_nasa_apod()
