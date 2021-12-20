from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

count_pay_key = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="5")
    ],
    [
        KeyboardButton(text="10")
    ],
    [
        KeyboardButton(text="20")
    ],
    [
        KeyboardButton(text="В главное меню⬅")
    ]
], resize_keyboard=True)