from aiogram.utils import executor
from bot_creation import dp


async def on_startup(_):
    print("Bot ONLINE!")


async def on_shutdown(_):
    print("Bot OFFLINE!")


from handlers import common
from handlers import wb
from handlers import lamoda


common.register_common_handlers(dp)
wb.register_wb_handlers(dp)
lamoda.register_la_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
