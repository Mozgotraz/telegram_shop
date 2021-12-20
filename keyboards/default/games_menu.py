from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

games_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="GTA V | 3 руб💿")
    ],
    [
        KeyboardButton(text="Far Cry 6 | 4 руб💿")
    ],
    [
        KeyboardButton(text="Назад⬅")
    ]
], resize_keyboard=True)
