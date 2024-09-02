import argparse
import os

from dotenv import load_dotenv
from telegram import Bot


def send_photo(bot, chat_id, photo_path):
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo,
                       caption="Вот вам картинка!")
    print("Сообщение и изображение отправлены!")


def main():
    load_dotenv()

    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    group_chat_id = os.getenv('TELEGRAM_CHANNEL_ID')

    bot = Bot(token=bot_token)

    parser = argparse.ArgumentParser(
        description='Отправка изображения в Telegram.')
    parser.add_argument('photo_path', type=str,
                        help='Путь к файлу с изображением')
    args = parser.parse_args()

    try:
        send_photo(bot, group_chat_id, args.photo_path)
    except FileNotFoundError:
        print(f"Файл не найден: {args.photo_path}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    main()
