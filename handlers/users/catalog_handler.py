from loader import dp
from aiogram import types
from keyboards import mac_menu_keyboard, kfc_menu_keyboard, vpn_menu_keyboard, games_menu_keyboard, catalog, \
    yandex_menu_keyboard


@dp.message_handler(text="McDonald’s🍔")
async def account_vpn(message: types.Message):
    await message.answer(f"📦Выберите товар", reply_markup=mac_menu_keyboard)


@dp.message_handler(text="KFC🍗")
async def account_games(message: types.Message):
    await message.answer(f"📦Выберите товар", reply_markup=kfc_menu_keyboard)


@dp.message_handler(text="VPN📡")
async def food(message: types.Message):
    await message.answer(f"📦Выберите товар", reply_markup=vpn_menu_keyboard)


@dp.message_handler(text="Аккаунты с играми📔")
async def other(message: types.Message):
    await message.answer(f"📦Выберите товар", reply_markup=games_menu_keyboard)


@dp.message_handler(text="Яндекс Еда🍞")
async def other(message: types.Message):
    await message.answer(f"📦Выберите товар", reply_markup=yandex_menu_keyboard)


@dp.message_handler(text="Назад⬅")
async def back(message: types.Message):
    await message.answer(f"{message.text}", reply_markup=catalog)
