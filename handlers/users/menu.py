import sqlite3
from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp
from keyboards.default import menu, catalog, balance_menu_keyboard
from keyboards.inline import support_keyboard
from aiogram.types import ParseMode, CallbackQuery
from utils import check_balance
from handlers.users import catalog_handler, pay_item, up_balance


@dp.message_handler(Command("start"))
async def main_menu(message: types.Message):
    check_user_id = []
    user_id = str(message.from_user.id)
    db = sqlite3.connect("user_data.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS {}(name varchar(255), balance INTEGER)".format('userss'))
    db.commit()
    sqlite_select_query = f"""SELECT * from userss WHERE name={user_id}"""
    cursor.execute(sqlite_select_query)
    x = cursor.fetchall()

    for i in x:
        print(i)
        check_user_id.append(i[0])

    print(check_user_id)

    if user_id in check_user_id:
        await message.answer(f"Добро пожаловать, {message.from_user.first_name}🤚!", reply_markup=menu)
        print("Да")
    else:
        cursor.execute("INSERT INTO userss VALUES (?,?)", (user_id, 0,))
        db.commit()
        await message.answer(f"Добро пожаловать, {message.from_user.first_name}🤚!", reply_markup=menu)
        print("Нет")


@dp.message_handler(Command("catalog"))
async def catalog_product(message: types.Message):
    await message.answer("💡Выберите категорию", reply_markup=catalog)


@dp.message_handler(Command("info"))
async def user_info(message: types.Message):
    user_id = str(message.from_user.id)
    user_balance = check_balance(user_id=user_id)
    await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖"
                         f"\nℹ<b>Информация о вас:</b>"
                         f"\n📜Логин: @{message.from_user.username}"
                         f"\n🔑ID: <b>{message.from_user.id}</b>"
                         f"\n\n\n💰Баланс: <b>{user_balance}</b> руб"
                         f"\n➖➖➖➖➖➖➖➖➖➖➖",
                         parse_mode=ParseMode.HTML)


@dp.message_handler(Command("balance"))
async def balance(message: types.Message):
    user_id = str(message.from_user.id)
    user_balance = check_balance(user_id=user_id)
    await message.answer(f"💰Баланс: <b>{user_balance}</b> руб.",
                         parse_mode=ParseMode.HTML,
                         reply_markup=balance_menu_keyboard)


@dp.message_handler(Command("support"))
@dp.message_handler(text="Поддержка🌐")
async def support(message: types.Message):
    await message.answer("🧑‍🔧Возникли проблемы?"
                         "\nНапишите в нашу службу поддержки!", reply_markup=support_keyboard)

@dp.message_handler(text="Каталог товаров🛒")
async def catalog_product(message: types.Message):
    await message.answer("💡Выберите категорию", reply_markup=catalog)


@dp.message_handler(text="Личный кабинет👤")
async def user_info(message: types.Message):
    user_id = str(message.from_user.id)
    user_balance = check_balance(user_id=user_id)
    await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖"
                         f"\nℹ<b>Информация о вас:</b>"
                         f"\n📜Логин: @{message.from_user.username}"
                         f"\n🔑ID: <b>{message.from_user.id}</b>"
                         f"\n\n\n💰Баланс: <b>{user_balance}</b> руб"
                         f"\n➖➖➖➖➖➖➖➖➖➖➖",
                         parse_mode=ParseMode.HTML)


@dp.message_handler(text="Баланс💰")
async def balance(message: types.Message):
    user_id = str(message.from_user.id)
    user_balance = check_balance(user_id=user_id)
    await message.answer(f"💰Баланс: <b>{user_balance}</b> руб.",
                         parse_mode=ParseMode.HTML,
                         reply_markup=balance_menu_keyboard)


@dp.message_handler(text="Поддержка🌐")
async def support(message: types.Message):
    await message.answer("🧑‍🔧Возникли проблемы?"
                         "\nНапишите в нашу службу поддержки!", reply_markup=support_keyboard)


@dp.message_handler(text="В главное меню⬅")
async def undo(message: types.Message):
    await message.answer(f"{message.text}", reply_markup=menu)


@dp.callback_query_handler(text="rules")
async def get_rules(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("1. Гарантия на аккаунты 15 минут. Вы должны потратить баланс за это время."
                              "\n1.1. Претензии по аккаунтам принимаются не позднее 15 минут после покупки."
                              "\n1.2. При передаче данных аккаунта третим лицам гарантия не действует."
                              "\n2. Все проблемные ситуации рассматриваются только при наличии записи экрана без "
                              "обрезки и монтажа."
                              "\n2.1. Видео должно начинаться перед началом покупки аккаунта до получения данных для "
                              "входа и длиться до траты баланса."
                              "\n2.2. На видео должна быть полностью видна ссылка по которой вы заходите")





