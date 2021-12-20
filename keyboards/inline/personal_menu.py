from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

personal_keyboard = InlineKeyboardMarkup(row_width=1,
                                         inline_keyboard=[
                                             [
                                                 InlineKeyboardButton(text="Реферальная система👥",
                                                                      callback_data="ref")
                                             ]
                                         ])