import os

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
group_chat_id = os.getenv('TELEGRAM_CHANNEL_ID')

bot = Bot(token=bot_token)

bot.send_message(chat_id=group_chat_id, text="Привет, группа!")

photo_path = 'images/spacex_launch_11.jpg'

try:
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=group_chat_id, photo=photo,
                       caption="Вот вам картинка!")
    print("Сообщение и изображение отправлены!")
except FileNotFoundError:
    print(f"Файл не найден: {photo_path}")
