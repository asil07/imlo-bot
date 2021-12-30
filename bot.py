"""
 2This is a echo bot.
 3It echoes any incoming text messages.
 4"""

import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWord
import os

API_TOKEN = os.getenv("TOKEN")


# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Imlo botga xush kelibsiz @asil_muhammadiy")


@dp.message_handler(commands=["help"])
async def send_info(message: types.Message):
    """ Bu funksiya yordam uchun malumotlar junatadi.
    """
    await message.reply("O'zbek tilidagi so'zlar imlo xatosini topuvchi bot")


@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    result = checkWord(word)
    if result["mavjud"]:
        resp = f"✅ {word.capitalize()}"
    else:
        resp = f"❌ {word.capitalize()}\n"
        for text in result["so'zlar"]:
            resp += f'✅ {text.capitalize()}'

    resp += "\n\n Murojaat uchun👇\n@asil_muhammadiy"
    await message.answer(resp)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
