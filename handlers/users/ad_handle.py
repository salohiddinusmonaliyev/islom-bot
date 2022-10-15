from aiogram.types import Message
from loader import dp, bot

@dp.message_handler()
async def ad():
    await bot.send_message(chat_id=None, text="Reklama")
