from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler
)

import requests

TOKEN = "6919722887:AAFZNrEdxEIh6mxLj1VYSgocMvDFlB9mTMA"

users = {}


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




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = []
    user.append(update.effective_user.first_name)
    user.append(update.effective_user.id)

    users[f"user-{update.effective_user.id}"] = user
    await update.message.reply_html(f'Assalomu alaykum {update.effective_user.first_name}\n\n<i>Botdagi foydalanuvchilar soni: {len(users)}</i>', reply_markup=regions_keyboard)


async def admin_handler(update: Update, context):

    message = update.message.text
    split_message = message.split(" ")

    text_after_admin = " ".join(split_message[1:])

    for key, value in users.items():
        user_id = value[1]
        await context.bot.send_message(chat_id=user_id, text=f"{text_after_admin}")

async def send_times(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    response = requests.get(f"https://islomapi.uz/api/present/day?region={query.data}")
    json_data = response.json()
    region = json_data["region"]
    date = json_data["date"]
    weekday = json_data["weekday"]
    month = json_data["hijri_date"]["month"]
    hijri_date = f"{json_data["hijri_date"]["day"]} {month.capitalize()}"
    times = json_data["times"]
    saharlik = times["tong_saharlik"]
    quyosh = times["quyosh"]
    peshin = times["peshin"]
    asr = times["asr"]
    shom = times["shom_iftor"]
    hufton = times["hufton"]

    message = f"""
Namoz vaqtlari 2️⃣0️⃣2️⃣4️⃣

🌆 {region}

{date} | {hijri_date} | {weekday}

Bomdod (Saharlik): {saharlik}
Quyosh: {quyosh}
Peshin: {peshin}
Asr: {asr}
Shom (Iftor): {shom}
Xufton: {hufton}

@{context.bot.username}
"""
    share_button = [
        [InlineKeyboardButton("Ulashish", switch_inline_query=message)]
    ]
    await query.edit_message_text(text=message, reply_markup=InlineKeyboardMarkup(share_button), parse_mode="HTML")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Viloyatni tanlang", reply_markup=regions_keyboard)
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("admin", admin_handler))

    application.add_handler(CallbackQueryHandler(send_times))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()