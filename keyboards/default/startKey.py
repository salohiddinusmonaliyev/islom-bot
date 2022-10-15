from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn1 = KeyboardButton("🕌 Namoz Vaqtlari")
btn2 = KeyboardButton("✨ Quron")
btn3 = KeyboardButton("📖 Payg'ambarimiz mo'jizalari")
btn4 = KeyboardButton("📘 Quron tafsiri")
btn5 = KeyboardButton("📗 Payg'ambarlar tarixi")

startkey = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1, btn3).add(btn2, btn4).add(btn5)
