from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


support_keyboard = InlineKeyboardMarkup(row_width=1,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(text="✉Обратиться в поддержку",
                                                                     callback_data="sup",
                                                                     url="https://t.me/mozgotras")
                                            ],
                                            [
                                                InlineKeyboardButton(text="❓Правила",
                                                                     callback_data="rules")
                                            ]
                                        ])
