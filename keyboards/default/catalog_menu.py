from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

catalog = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="McDonald’s🍔")
        ],

        [
            KeyboardButton(text="KFC🍗")
        ],

        [
          KeyboardButton(text="VPN📡")
        ],

        [
            KeyboardButton(text="Аккаунты с играми📔")
        ],
        [
          KeyboardButton(text="Яндекс Еда🍞")
        ],

        [
            KeyboardButton(text="В главное меню⬅")
        ]
    ],
    resize_keyboard=True
)
