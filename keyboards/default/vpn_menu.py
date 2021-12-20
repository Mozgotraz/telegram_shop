from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

vpn_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Nord VPN 365 дней | 3 руб🖥")
    ],
    [
        KeyboardButton(text="ZenMate 3 месяца | 4 руб🖥")
    ],
    [
        KeyboardButton(text="Назад⬅")
    ]
], resize_keyboard=True)
