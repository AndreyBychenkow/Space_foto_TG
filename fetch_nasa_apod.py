import os

import requests
from dotenv import load_dotenv

from common_functions import get_file_extension, download_image

NASA_APOD_COUNT = 20


def fetch_nasa_apod_images(api_key, count=NASA_APOD_COUNT):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': api_key, 'count': count}
    response = requests.get(url, params=params)
    response.raise_for_status()
    photos_data = response.json()
    return [item['url'] for item in photos_data]


def main():
    load_dotenv()
    nasa_api_key = os.environ.get('API_TOKEN_NASA')
    if not nasa_api_key:
        print("API_TOKEN_NASA не найден в переменных окружения.")
        return
    try:
        image_urls = fetch_nasa_apod_images(nasa_api_key)
        print(f"Ссылки на фото дня NASA: {image_urls}")
        folder_name = 'nasa_apod_images'
        os.makedirs(folder_name, exist_ok=True)
        for index, image_url in enumerate(image_urls, start=1):
            file_extension = get_file_extension(image_url)
            file_path = os.path.join(folder_name, f"{index}{file_extension}")
            download_image(image_url, file_path)
        print(f'Фото дня NASA сохранены в папке: {folder_name}')
    except requests.exceptions.RequestException as request_error:
        print(f"Ошибка при выполнении запроса: {request_error}")
    except FileNotFoundError as file_error:
        print(f"Ошибка при сохранении файла: {file_error}")


if __name__ == '__main__':
    main()
