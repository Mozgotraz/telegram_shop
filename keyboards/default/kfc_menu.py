from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kfc_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Пати бокс | 3 руб🍟")
    ],
    [
        KeyboardButton(text="Чизбургер | 2 руб🍔")
    ],
    [
        KeyboardButton(text="Назад⬅")
    ]
], resize_keyboard=True)