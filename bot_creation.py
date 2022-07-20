from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from config import Configuration

bot = Bot(token=Configuration.token)
dp = Dispatcher(bot)