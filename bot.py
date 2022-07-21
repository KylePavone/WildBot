from aiogram.utils import executor
from bot_creation import dp


async def on_startup(_):
    print("Bot ONLINE!")


from handlers import common
from handlers import func


common.register_common_handlers(dp)
func.register_func_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
