from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler
)
from bs4 import BeautifulSoup
import requests

from datetime import datetime
from hijri_converter import convert

import time

TOKEN = "6919722887:AAHti0nVlkwVXfk5JtRRwP9ZSBWDOZ6d7_Q"

ADMIN = "6827107114"

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

def extract_text(text):
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.text.strip()
    return text

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = []
    user.append(update.effective_user.first_name)
    user.append(update.effective_user.id)
    join_key = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Namoz Vaqti | Uzbekistan", url="https://t.me/+y82Q9WLbt042M2Ey")
            ]
        ]
    )
    users[f"user-{update.effective_user.id}"] = user
    channel_id = "-1002073389981"
    if update.message:
        chat_id = update.message.chat_id
        member = await context.bot.get_chat_member(channel_id, chat_id)

        if update.effective_user.id == ADMIN or member.status == "creator":
            await update.message.reply_html(f'Assalomu alaykum admin!\n<i><b>Foydalanuvchilar soni: {len(users)}</b></i>', reply_markup=regions_keyboard)
        elif member.status == "member":
            await update.message.reply_html(f'<b>Assalomu alaykum {update.effective_user.first_name}!</b>\n\nViloyatlardan birini tanlang', reply_markup=regions_keyboard)
        elif str(member.status)=="left":
            await update.message.reply_html(f'<b>Assalomu alaykum {update.effective_user.first_name}!</b>\nAvval quyidagi kanalga obuna bo\'ling\n\n<i>Obuna bo\'lgach <b>/start</b> ni qaytadan bosing</i>', reply_markup=join_key)
    elif update.callback_query and update.callback_query.message:
        chat_id = update.callback_query.from_user.id
        member = await context.bot.get_chat_member(channel_id, chat_id)
        if update.effective_user.id == ADMIN or member.status == "creator":
            await update.callback_query.message.reply_html(f'Assalomu alaykum admin!\n<i><b>Foydalanuvchilar soni: {len(users)}</b></i>', reply_markup=regions_keyboard)
        elif member.status == "member":
            await update.callback_query.message.reply_html(f'<b>Assalomu alaykum {update.effective_user.first_name}!</b>\n\nViloyatlardan birini tanlang', reply_markup=regions_keyboard)
        elif str(member.status)=="left":
            await update.callback_query.message.reply_html(f'<b>Assalomu alaykum {update.effective_user.first_name}!</b>\nAvval quyidagi kanalga obuna bo\'ling\n\n<i>Obuna bo\'lgach <b>/start</b> ni qaytadan bosing</i>', reply_markup=join_key)

async def group_handler(update: Update, context):
    chat_id = "-1002073389981"
    cities = [
    "Andijon",
    "Buxoro",
    "Farg'ona",
    "Jizzax",
    "Urganch",
    "Namangan",
    "Navoiy",
    "Qarshi",
    "Nukus",
    "Samarqand",
    "Guliston",
    "Termiz",
    "Toshkent"
]
    for i in cities:
        response = requests.get(f"https://islomapi.uz/api/present/day?region={i}")
        json_data = response.json()
        region = json_data["region"]
        date = json_data["date"]
        weekday = json_data["weekday"]
        month = json_data["hijri_date"]["month"]
        times = json_data["times"]
        saharlik = times["tong_saharlik"]
        quyosh = times["quyosh"]
        peshin = times["peshin"]
        asr = times["asr"]
        shom = times["shom_iftor"]
        hufton = times["hufton"]
        war = datetime.strptime(date, '%Y-%m-%d')
        war1 = convert.Gregorian.fromdate(war).to_hijri()
        hijri_year = war1.year
        hijri_date = war1.day
        hijri_month = war1.month_name()
        message = f"""<b>
Namoz vaqtlari 2️⃣0️⃣2️⃣4️⃣

🌆 {region}

{date} | {hijri_year}-yil {hijri_date}-{hijri_month} | {weekday}

Bomdod: {saharlik}
Quyosh: {quyosh}
Peshin: {peshin}
Asr: {asr}
Shom: {shom}
Xufton: {hufton}

<i>@{context.bot.username} | @namoz_vaqti_uzbekistan</i></b>
    """
        print(i)
        await context.bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")
        time.sleep(3)

async def admin_handler(update: Update, context):
    message = update.message.text
    message = message.replace('/admin ', '')
    for key, value in users.items():
        try:
            user_id = value[1]
            share_button = [
                [InlineKeyboardButton("✉️ Ulashish", switch_inline_query=extract_text(message))]
            ]
            await context.bot.send_message(chat_id=user_id, text=f"{message}\n\n<span class='tg-spoiler'><i>@{context.bot.username} | @namoz_vaqti_uzbekistan</i></span>", parse_mode="HTML", reply_markup=InlineKeyboardMarkup(share_button))
        except Exception as e:
            print("Failed to send message to user: %s", e)


async def send_times(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query.data == "back":
        message_id = context.user_data.get("message")
        await context.bot.deleteMessage(chat_id=query.from_user.id, message_id=message_id)
        return await start(update, context)
    else:
        response = requests.get(f"https://islomapi.uz/api/present/day?region={query.data}")
        json_data = response.json()
        region = json_data["region"]
        date = json_data["date"]
        weekday = json_data["weekday"]
        month = json_data["hijri_date"]["month"]
        times = json_data["times"]
        saharlik = times["tong_saharlik"]
        quyosh = times["quyosh"]
        peshin = times["peshin"]
        asr = times["asr"]
        shom = times["shom_iftor"]
        hufton = times["hufton"]
        war = datetime.strptime(date, '%Y-%m-%d')
        war1 = convert.Gregorian.fromdate(war).to_hijri()
        hijri_year = war1.year
        hijri_date = war1.day
        hijri_month = war1.month_name()
        message = f"""<b>
Namoz vaqtlari 2️⃣0️⃣2️⃣4️⃣

🌆 {region}

{date} | {hijri_year}-yil {hijri_date}-{hijri_month} | {weekday}

Bomdod: {saharlik}
Quyosh: {quyosh}
Peshin: {peshin}
Asr: {asr}
Shom: {shom}
Xufton: {hufton}

<i>@{context.bot.username} | @namoz_vaqti_uzbekistan</i></b>
    """
        share_button = [
            [
                InlineKeyboardButton("✉️ Ulashish", switch_inline_query=f'\n\n\n{extract_text(message).replace("@namozvaqti_uzbekistan_bot", "")}'),
            ],
            [
                InlineKeyboardButton("🔙 Ortga", callback_data="back")
            ]
        ]
        msg = await query.edit_message_text(text=message, reply_markup=InlineKeyboardMarkup(share_button), parse_mode="HTML")
        context.user_data["message"] = msg.id
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("admin", admin_handler))
    application.add_handler(CommandHandler("group", group_handler))

    application.add_handler(CallbackQueryHandler(send_times))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
