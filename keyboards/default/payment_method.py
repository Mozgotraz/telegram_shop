from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils import check_balance
from aiogram import types

# balance = 0
#
# async def get_balance(message: types.Message):
#     global balance
#     user = message.from_user.id
#     balance = check_balance(user_id=user)
#     print(balance)



payment_method_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text=f"Снять с баланса💰")
    ],
    [
        KeyboardButton(text="Оплатить QIWI🥝")
    ],
    [
        KeyboardButton(text="Отменить❌")
    ]
], resize_keyboard=True)