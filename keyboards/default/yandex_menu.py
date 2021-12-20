from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

yandex_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Промокод на 250 рублей | 2 руб🥪")
    ],
    [
        KeyboardButton(text="Промокод на 500 рублей | 4 руб🥪")
    ],
    [
        KeyboardButton(text="Назад⬅")
    ]
], resize_keyboard=True)