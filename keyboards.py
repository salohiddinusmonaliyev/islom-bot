from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup([
    ["Namoz vaqtlari"]
], resize_keyboard=True)

regions_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Andijon", callback_data="Andijon"),
            InlineKeyboardButton("Buxoro", callback_data="Buxoro"),
        ],
        [
            InlineKeyboardButton("Farg'ona", callback_data="Farg'ona"),
            InlineKeyboardButton("Jizzax", callback_data="Jizzax"),
        ],
        [
            InlineKeyboardButton("Xorazm", callback_data="Urganch"),
            InlineKeyboardButton("Namangan", callback_data="Namangan"),
        ],
        [
            InlineKeyboardButton("Navoiy", callback_data="Navoiy"),
            InlineKeyboardButton("Qashqadaryo", callback_data="Qarshi"),
        ],
        [
            InlineKeyboardButton("Qoraqalpogʻiston", callback_data="Nukus"),
            InlineKeyboardButton("Samarqand", callback_data="Samarqand"),
        ],
        [
            InlineKeyboardButton("Sirdaryo", callback_data="Guliston"),
            InlineKeyboardButton("Surxondaryo", callback_data="Termiz"),
        ],
        [InlineKeyboardButton("Toshkent", callback_data="Toshkent"),]
    ]
)
