import os
from datetime import datetime

import requests
from dotenv import load_dotenv

from common_functions import download_image


def fetch_earth_epic_photo_urls(api_key, num_photos=5):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)

    if response.status_code == 403:
        raise PermissionError(
            "Ошибка 403: Доступ запрещен. Проверьте ваш API ключ.")

    response.raise_for_status()
    photos_data = response.json()

    selected_photos = photos_data[:num_photos]
    photo_urls = []
    for photo in selected_photos:
        date = datetime.fromisoformat(photo['date'])
        photo_url = (f"https://epic.gsfc.nasa.gov/archive/natural/{date.year}/"
                     f"{date.month:02}/{date.day:02}/png/{photo['image']}.png")
        photo_urls.append(photo_url)

    return photo_urls


def main():
    load_dotenv()
    nasa_api_key = os.environ.get('API_TOKEN_NASA')

    if not nasa_api_key:
        print("API_TOKEN_NASA не найден в переменных окружения.")
        return

    try:
        photo_urls = fetch_earth_epic_photo_urls(nasa_api_key, num_photos=5)
        print(f"Ссылки на фото Земли: {photo_urls}")

        folder_name = 'earth_epic_photos'
        os.makedirs(folder_name, exist_ok=True)

        for index, photo_url in enumerate(photo_urls, start=1):
            file_path = os.path.join(folder_name, f"earth_epic_{index}.png")
            download_image(photo_url, file_path)
        print(f'Фото Земли сохранены в папке: {folder_name}')
    except requests.exceptions.RequestException as request_error:
        print(f"Ошибка при выполнении запроса: {request_error}")
    except PermissionError as permission_error:
        print(
            f"Ошибка доступа: {permission_error}. Неправильный API ключ или отсутствие прав доступа.")
    except FileNotFoundError as file_error:
        print(f"Ошибка при сохранении файла: {file_error}")


if __name__ == '__main__':
    main()
