import os

from dotenv import load_dotenv
from telegram import Bot


def send_photo(bot, chat_id, photo_path):
    try:
        with open(photo_path, 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo,
                           caption="Вот вам картинка!")
        print("Сообщение и изображение отправлены!")
    except FileNotFoundError:
        print(f"Файл не найден: {photo_path}")


def main():
    load_dotenv()

    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    group_chat_id = os.getenv('TELEGRAM_CHANNEL_ID')

    bot = Bot(token=bot_token)

    photo_path = input("Введите путь к файлу с изображением: ")

    send_photo(bot, group_chat_id, photo_path)


if __name__ == '__main__':
    main()
