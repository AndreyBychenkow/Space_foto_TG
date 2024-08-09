import argparse
import os

import requests
from dotenv import load_dotenv

from common_functions import get_file_extension, download_image


def get_launch_photos(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data.get('links', {}).get('flickr', {}).get('original', [])


def fetch_spacex_launch_photos(launch_id):
    try:
        photo_urls = get_launch_photos(launch_id)

        if not photo_urls:
            print("Нет фотографий для этого запуска SpaceX.")
            return

        folder_name = 'spacex_images'
        os.makedirs(folder_name, exist_ok=True)

        for i, url in enumerate(photo_urls):
            file_extension = get_file_extension(url)
            file_path = os.path.join(folder_name,
                                     f'spacex_launch_{i + 1}{file_extension}')
            download_image(url, file_path)

        print(f'Все изображения SpaceX сохранены в папке: {folder_name}')
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
    except FileNotFoundError as e:
        print(f"Ошибка при сохранении файла: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='Скачивание фотографий SpaceX.')
    parser.add_argument('--launch_id', type=str, help='ID запуска SpaceX')

    args = parser.parse_args()
    load_dotenv()

    launch_id = args.launch_id if args.launch_id else '5eb87d46ffd86e000604b388'
    fetch_spacex_launch_photos(launch_id)


if __name__ == '__main__':
    main()
