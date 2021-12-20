from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text="Каталог товаров🛒")
        ],

        [
            KeyboardButton(text="Личный кабинет👤")
        ],

        [
            KeyboardButton(text="Баланс💰")
        ],

        [
            KeyboardButton(text="Поддержка🌐")
        ]
    ],
    resize_keyboard=True
)
