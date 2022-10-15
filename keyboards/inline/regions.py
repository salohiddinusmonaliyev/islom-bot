from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

region_keys = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🏙 Toshkent", callback_data="Toshkent"),
        InlineKeyboardButton(text="🏙 Farg'ona", callback_data="Farg%27оna"),
    ],
    [
        InlineKeyboardButton(text="🏙 Andijon", callback_data="Toshkent"),
        InlineKeyboardButton(text="🏙 Namangan", callback_data="Farg%27оna"),
    ],
    [
        InlineKeyboardButton(text="🏙 Samarqand", callback_data="Toshkent"),

    ],
    [
        InlineKeyboardButton(text="✉ Uashish", switch_inline_query="Namoz vaqtlari, Qurondagi 50 ta surani audiosi, Payg'ambarimiz mo'jizalari, Payg'ambarlar tarixini bilish uchun bot"),
    ],
    [
      InlineKeyboardButton("🔙 Bosh Menyu", callback_data="mainmenu")
    ],
])
