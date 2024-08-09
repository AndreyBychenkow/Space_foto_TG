# Космический Телеграм

### Этот проект представляет собой Telegram-бота, который автоматически публикует фотографии из заданной директории в указанную группу Telegram с заданным интервалом и повторяет их в случайном порядке, если все фото были опубликованы.

## Как установить

### Шаг 1: Получение ключей

1. Токен бота Telegram: Получите его, создав бота в BotFather в Telegram. Сохраните токен, который предоставит BotFather. Добавьте бота в вашу группу и дайте ему права администратора.
2. ID вашей группы:  Откройте группу в приложении Telegram и нажмите на название группы в верхней части экрана. Идентификатор группы будет отображаться в адресной строке вашего браузера.

### Шаг 2: Создание файла конфигурации

Создайте файл .env в корневом каталоге вашего проекта и добавьте в него следующие строки, заменив значения на свои:

```makefile
TELEGRAM_BOT_TOKEN=ваш_токен_бота
TELEGRAM_CHANNEL_ID=ваш_ID_группы
```

### Шаг 3: Установка зависимостей

Python 3 должен быть установлен. Затем используйте pip для установки необходимых зависимостей. В корневом каталоге проекта выполните команду:

```bash
pip install -r requirements.txt
```

### Шаг 4: Как использовать

1. Убедитесь, что вы настроили переменные окружения в .env файле.
2. Проверьте, что директория с фотографиями существует и содержит изображения.
3. Запустите скрипт с помощью Python:
```bash
python bot_info.py
```

Бот начнет публиковать фотографии в вашей группе с заданным интервалом.

