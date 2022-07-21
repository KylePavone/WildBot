from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot_creation import bot
from parsers.wildberries.wb_parse import pages


class FSMWbParser(StatesGroup):
    brand = State()


async def starting(message: types.Message):
    await FSMWbParser.brand.set()
    await message.reply("Введи название бренда кроссовок:")


async def get_choose(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["brand"] = message.text
    await message.reply("Подожди...")
    async with state.proxy() as data:
        for i in range(5):
            answer = pages(data["brand"])[0][i]
            await bot.send_message(message.from_user.id, answer)
    await state.finish()


def register_wb_handlers(dp: Dispatcher):
    dp.register_message_handler(starting, commands=["wildberries"], state=None)
    dp.register_message_handler(get_choose, content_types=["text"], state=FSMWbParser.brand)
