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
    images_metadata = response.json()

    selected_images_metadata = images_metadata[:num_photos]
    image_urls = []

    for image_metadata in selected_images_metadata:
        date = datetime.strptime(image_metadata['date'], '%Y-%m-%d %H:%M:%S')
        image_url = (f"https://epic.gsfc.nasa.gov/archive/natural/{date.year}/"
                     f"{date.month:02}/{date.day:02}/png/{image_metadata['image']}.png")
        image_urls.append(image_url)

    return image_urls


def main():
    load_dotenv()
    nasa_api_key = os.environ.get('API_TOKEN_NASA')

    if not nasa_api_key:
        print("API_TOKEN_NASA не найден в переменных окружения.")
        return

    try:
        image_urls = fetch_earth_epic_photo_urls(nasa_api_key, num_photos=5)
        print(f"Ссылки на фото Земли: {image_urls}")

        folder_name = 'earth_epic_photos'
        os.makedirs(folder_name, exist_ok=True)

        for index, image_url in enumerate(image_urls, start=1):
            file_path = os.path.join(folder_name, f"earth_epic_{index}.png")
            download_image(image_url, file_path)
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
