from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

balance_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Пополение QIWI🥝")
    ],
    [
        KeyboardButton(text="В главное меню⬅")
    ]
], resize_keyboard=True)
