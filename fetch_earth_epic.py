import os

import requests
from dotenv import load_dotenv

from common_functions import download_image


def get_earth_epic_photos(api_key, num_photos=5):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)

    if response.status_code == 403:
        raise PermissionError(
            "Ошибка 403: Доступ запрещен. Проверьте ваш API ключ.")

    response.raise_for_status()
    data = response.json()

    photos = data[:num_photos]
    photo_urls = [
        (f"https://epic.gsfc.nasa.gov/archive/natural/{photo['date'][:4]}/"
         f"{photo['date'][5:7]}/{photo['date'][8:10]}/png/{photo['image']}.png")
        for photo in photos
    ]

    return photo_urls


def fetch_earth_epic_photos():
    load_dotenv()
    api_token_nasa = os.environ.get('API_TOKEN_NASA')

    if not api_token_nasa:
        print("API_TOKEN_NASA не найден в переменных окружения.")
        return

    try:
        photo_urls = get_earth_epic_photos(api_token_nasa, num_photos=5)
        print(f"Ссылки на фото Земли: {photo_urls}")

        folder_name = 'earth_epic_photos'
        os.makedirs(folder_name, exist_ok=True)

        for i, url in enumerate(photo_urls):
            file_path = os.path.join(folder_name, f"earth_epic_{i + 1}.png")
            download_image(url, file_path)
        print(f'Фото Земли сохранены в папке: {folder_name}')
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
    except PermissionError as e:
        print(
            f"Ошибка доступа: {e}. Неправильный API ключ или отсутствие прав доступа.")
    except FileNotFoundError as e:
        print(f"Ошибка при сохранении файла: {e}")


if __name__ == '__main__':
    fetch_earth_epic_photos()
