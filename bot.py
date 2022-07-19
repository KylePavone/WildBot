from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import Configuration
from main import pages


bot = Bot(token=Configuration.token)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message: types.message):
    await bot.send_message(message.from_user.id, "Searching...")
    if message.text == "sales":
        answer = pages("adidas")[0][0]
        await bot.send_message(message.from_user.id, answer)
    else:
        answer = "Напиши 'скидки'"
        await bot.send_message(message.from_user.id, answer)


executor.start_polling(dp, skip_updates=True)
