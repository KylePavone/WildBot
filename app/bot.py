from aiogram.utils import executor
from bot_creation import dp


async def on_startup(_):
    print("Bot ONLINE!")


async def on_shutdown(_):
    print("Bot OFFLINE!")


from handlers import common_handler
from handlers import wildberries_handler
from handlers import lamoda_handler


common_handler.register_common_handlers(dp)
wildberries_handler.register_wb_handlers(dp)
lamoda_handler.register_la_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
