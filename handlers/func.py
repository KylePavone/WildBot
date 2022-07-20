from aiogram import types
from aiogram import Dispatcher

from bot_creation import bot

from parsers.wildberries.wb_parse import pages


async def search_wildberries(message: types.message):
    await bot.send_message(message.from_user.id, "Searching...")
    if message.text == "sales":
        for i in range(5):
            answer = pages("adidas")[0][i]
            await bot.send_message(message.from_user.id, answer)
    else:
        answer = 'Send "sales"'
        await bot.send_message(message.from_user.id, answer)


def register_func_handlers(dp: Dispatcher):
    dp.register_message_handler(search_wildberries)
