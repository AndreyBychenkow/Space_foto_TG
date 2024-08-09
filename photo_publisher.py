import os
import random
import time

from dotenv import load_dotenv
from telegram import Bot


def publish_photos(directory, delay, bot_token, group_chat_id):
    bot = Bot(token=bot_token)

    while True:
        photos = [os.path.join(directory, file) for file in
                  os.listdir(directory) if
                  file.lower().endswith(('jpg', 'jpeg', 'png'))]

        random.shuffle(photos)

        for photo_path in photos:
            with open(photo_path, 'rb') as photo:
                bot.send_photo(chat_id=group_chat_id, photo=photo,
                               caption="Вот вам картинка!")
            print(f"Сообщение и изображение отправлены: {photo_path}")
            time.sleep(delay * 3600)


def main():
    directory = 'photo_of_the_day'
    delay = 4

    load_dotenv()

    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    group_chat_id = os.getenv('TELEGRAM_CHANNEL_ID')

    if bot_token and group_chat_id and os.path.isdir(directory):
        publish_photos(directory, delay, bot_token, group_chat_id)
    else:
        print("Проверьте переменные окружения и директорию.")


if __name__ == "__main__":
    main()
