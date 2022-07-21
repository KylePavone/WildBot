from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot_creation import bot
from parsers.lamoda.lamoda_parse import lm_parse

class FSMLaParser(StatesGroup):
    brand = State()


async def startings(message: types.Message):
    await FSMLaParser.brand.set()
    await message.reply("Введи название бренда кроссовок:")


async def get_chosen(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["brand"] = message.text
    await message.reply("Подожди...")

    async with state.proxy() as data:
        for i in range(5):
            answer = lm_parse(data["brand"])[i]
            await bot.send_message(message.from_user.id, answer)

    await state.finish()


def register_la_handlers(dp: Dispatcher):
    dp.register_message_handler(startings, commands=["lamoda"], state=None)
    dp.register_message_handler(get_chosen, content_types=["text"], state=FSMLaParser.brand)
