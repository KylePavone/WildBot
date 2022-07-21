from aiogram import types
from aiogram import Dispatcher

from bot_creation import bot
from keyboards import common_keyboard


async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "I'm bot-searcher", reply_markup=common_keyboard)
    await message.delete()


async def about_command(message: types.Message):
    await bot.send_message(message.from_user.id, "I'm bot-searcher,\nI was built for searching your 'cheap' shoes\n")
    await message.delete()


def register_common_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start", "help"])
    dp.register_message_handler(about_command, commands=["about"])
