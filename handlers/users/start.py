from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.startKey import startkey
from loader import dp, bot


# @dp.message_handler(CommandStart(deep_link=))
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!")

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b>Assalomu aleykum, {message.from_user.full_name}!</b>\nSiz bu bot orqali <b>Namoz vaqtlari, Qurondagi 50 ta surani audiosi, Payg'ambarimiz mo'jizalari, Payg'ambarlar tarixi</b>ni bilib olishingiz mumkin.", reply_markup=startkey)
    id = message.from_user.id

