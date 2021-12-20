from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# def buy_key(item_id):
#     key = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [
#                 InlineKeyboardButton(text="Купить", callback_data=f"buy:{item_id}")
#             ]
#         ]
#     )

key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купить", callback_data=f"buy")
        ],
    ]
)

key2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купить", callback_data=f"buy2")
        ]
    ]
)

key3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купить", callback_data=f"buy3")
        ]
    ]
)

key4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купить", callback_data=f"buy4")
        ]
    ]
)

key5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купить", callback_data=f"buy5")
        ]
    ]
)

key6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купить", callback_data=f"buy6")
        ]
    ]
)

key7 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купить", callback_data=f"buy7")
        ]
    ]
)

key8 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купить", callback_data=f"buy8")
        ]
    ]
)

key9 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купить", callback_data=f"buy9")
        ]
    ]
)

key10 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купить", callback_data=f"buy10")
        ]
    ]
)

key_k = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Оплатил", callback_data="paid")
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ]
)

key_pay_balance = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Оплатил", callback_data="paid_balance")
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ]
)

