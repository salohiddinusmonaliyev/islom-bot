from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove

from keyboards.default.startKey import startkey
from keyboards.inline.mujizalar_keys import mujizaKey
from keyboards.inline.quran_keys import quranKey
from keyboards.inline.regions import region_keys
from loader import dp, bot

import requests


@dp.message_handler(text=["✨ Quron"])
async def func1(message: Message):
    await message.answer(f"Quron :", reply_markup=quranKey)


@dp.message_handler(text=["🕌 Namoz Vaqtlari"])
async def func(message: Message):
    await message.answer(f"Namoz Vaqtlari :", reply_markup=region_keys)


@dp.message_handler(text=["📖 Payg'ambarimiz mo'jizalari"])
async def func(message: Message):
    await message.answer(f"Payg'ambarimiz mo'jizalari :", reply_markup=mujizaKey)


@dp.callback_query_handler(text=["Farg%27оna", "Toshkent"])
async def prayer(call: CallbackQuery):
    call_data = call.data
    url = f"https://islomapi.uz/api/present/day?region={call_data}"
    r = requests.get(url)
    date = r.json()['date']
    week = r.json()['weekday']
    time = r.json()['times']
    saharlik = time['tong_saharlik']
    quyosh = time['quyosh']
    peshin = time['peshin']
    asr = time['asr']
    shom = time['shom_iftor']
    hufton = time['hufton']
    region = r.json()['region']
    msg = f"<b>Namoz vaqtlari 2️⃣0️⃣2️⃣2️⃣ </b>\n" \
          f"\n<b>{region} viloyati</b>\n" \
          f"\nSana: {date}\nKun: {week}" \
          f"\nBomdod: {saharlik}" \
          f"\nQuyosh: {quyosh}" \
          f"\nPeshin: {peshin}" \
          f"\nAsr: {asr}" \
          f"\nShom: {shom}" \
          f"\nXufton: {hufton}"
    await bot.send_message(chat_id=call.from_user.id, text=msg, reply_markup=ReplyKeyboardRemove())
    await bot.send_message(chat_id=call.from_user.id, text="Tanlang: ", reply_markup=region_keys)
    await call.answer(cache_time=60)


@dp.callback_query_handler(
    text=['700', "701", "702", "703", "704", "705", "706", "707", "708", "709", "710", "711", "712", "713", "714",
          "715", "716", "717", "718", "719", "720", "721", "722", "723", "724", "725", "726", "727", "728", "729",
          '730', "731", "732", "733", "734", "735", "736", "737", "738", "739", "740", "741", "742", "743", "744"])
async def quran(call: CallbackQuery):
    await bot.send_audio(chat_id=call.from_user.id, audio=f"https://t.me/Mishariy_Roshid_Alafasiy/{call.data}",
                         reply_markup=ReplyKeyboardRemove())
    await call.message.delete()
    await bot.send_message(chat_id=call.from_user.id, text=f"Tanlang: ", reply_markup=quranKey)
    await call.answer(cache_time=60)


# , "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31","32","33","34","35","36","37","38",
# "39","40","41","42","43","44","45","46","47","48","49","50","51","52","53"
@dp.callback_query_handler(
    text=["4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"])
async def mujiza(call: CallbackQuery):
    await bot.send_audio(chat_id=call.from_user.id, audio=f"https://t.me/bbotbaza/{call.data}")
    await call.message.delete()
    await bot.send_message(chat_id=call.from_user.id, text=f"Tanlang: ", reply_markup=mujizaKey)
    await call.answer(cache_time=60)
    # print(call.data)


@dp.callback_query_handler(
    text=["mainmenu"])
async def mainmenu(call: CallbackQuery):
    await call.message.delete()
    await bot.send_message(chat_id=call.from_user.id, text=f"Bosh Sahifaga qaytildi.", reply_markup=startkey)
    await call.answer(cache_time=60)
