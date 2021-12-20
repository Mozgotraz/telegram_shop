from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mac_menu_keyboard = ReplyKeyboardMarkup(
                              keyboard=[
                                  [
                                      KeyboardButton(text="Биг Мак | 4 руб🍔")
                                  ],
                                  [
                                      KeyboardButton(text="Картошка маленькая | 2 руб🍟")
                                  ],
                                  [
                                      KeyboardButton(text="Назад⬅")
                                  ]
                              ], resize_keyboard=True)