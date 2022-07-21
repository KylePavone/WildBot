from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from config import Configuration
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

bot = Bot(token=Configuration.token)
dp = Dispatcher(bot, storage=storage)
