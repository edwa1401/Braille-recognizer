import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='braille_rec_bot.log', level=logging.INFO, format="%(levelname)s:%(asctime)s - %(message)s")


def greet_user(update, context):
    update.message.reply_text("Здравствуйте. Прикрепите фото шрифта Брайля и отпраьте его, чтобы получить перевод.")


def check_user_photo(update, context):
    update.message.reply_text("Обрабатываем фото")
    os.makedirs("../downloads", exist_ok=True)
    photo_file = context.bot.getFile(update.message.photo[-1].file_id)
    filename = os.path.join("../downloads", f"{photo_file.file_id}.jpg")
    photo_file.download(filename)
    update.message.reply_text("Файл сохранён")


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.photo, check_user_photo))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
