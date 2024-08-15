import argparse
import os

import requests

from common_functions import get_file_extension, download_image


def fetch_launch_photos(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    launch_info = response.json()
    return launch_info.get('links', {}).get('flickr', {}).get('original', [])


def download_spacex_launch_photos(launch_id):
    try:
        photo_urls = fetch_launch_photos(launch_id)
        if not photo_urls:
            print("Нет фотографий для этого запуска SpaceX.")
            return
        folder_name = 'spacex_images'
        os.makedirs(folder_name, exist_ok=True)
        for photo_number, photo_url in enumerate(photo_urls, start=1):
            file_extension = get_file_extension(photo_url)
            file_name = f'spacex_launch_{photo_number}{file_extension}'
            file_path = os.path.join(folder_name, file_name)
            download_image(photo_url, file_path)
        print(f'Все изображения SpaceX сохранены в папке: {folder_name}')
    except requests.exceptions.RequestException as request_error:
        print(f"Ошибка при выполнении запроса: {request_error}")
    except FileNotFoundError as file_error:
        print(f"Ошибка при сохранении файла: {file_error}")


def main():
    parser = argparse.ArgumentParser(
        description='Скачивание фотографий SpaceX.')
    parser.add_argument('--launch_id', type=str, help='ID запуска SpaceX',
                        default='5eb87d46ffd86e000604b388')
    args = parser.parse_args()
    download_spacex_launch_photos(args.launch_id)


if __name__ == '__main__':
    main()
