from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot_creation import bot
from parsers.lamoda.lamoda_parse import lm_parse

class FSMLaParser(StatesGroup):
    brand = State()
    number = State()

async def starting(message: types.Message):
    await FSMLaParser.brand.set()
    await message.reply("Введи название бренда кроссовок:")


async def content(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["brand"] = message.text
    await message.reply("Введи количество ссылок: ")

    await FSMLaParser.next()

async def links_num(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["number"] = message.text
    await message.reply("Ищу...")


    async with state.proxy() as data:
        try:
            for i in range(int(data["number"])):
                answer = lm_parse(data["brand"])[i]
                await bot.send_message(message.from_user.id, answer)
        except IndexError:
            await bot.send_message(message.from_user.id, "А че то не находит)))")

    await state.finish()



def register_la_handlers(dp: Dispatcher):
    dp.register_message_handler(starting, commands=["lamoda"], state=None)
    dp.register_message_handler(content, content_types=["text"], state=FSMLaParser.brand)
    dp.register_message_handler(links_num, content_types=["text"], state=FSMLaParser.number)
