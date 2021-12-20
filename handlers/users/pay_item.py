from loader import dp
from aiogram import types
from data.item import items
from data.config import wallet_qiwi
from keyboards.inline.buy_menu import key, key2, key3, key4, key5, key6, key7, key8, key9, key10, key_k
from aiogram.types import CallbackQuery, ParseMode
from aiogram.dispatcher import FSMContext
from utils import Payment, NotEnoughMoney, NoPaymentFound, check_balance
from keyboards import menu,payment_method_keyboard, catalog
import sqlite3

item_id = 0
amount_from_balance = 0



@dp.message_handler(text_contains="руб")
async def get_item(message: types.Message):
    global item_id, amount_from_balance
    caption = """
<b>Название продукта:</b> {title}
<b>Описание:</b> {description}
<b>Цена:</b> {price:.2f} RUB
"""

    if message.text == "Биг Мак | 4 руб🍔":
        item_id = 1
        amount_from_balance = 4


    elif message.text == "Картошка маленькая | 2 руб🍟":
        item_id = 2
        amount_from_balance = 2

    elif message.text == "Пати бокс | 3 руб🍟":
        item_id = 3
        amount_from_balance = 3

    elif message.text == "Чизбургер | 2 руб🍔":
        item_id = 4
        amount_from_balance = 2

    elif message.text == "Nord VPN 365 дней | 3 руб🖥":
        item_id = 5
        amount_from_balance = 3

    elif message.text == "ZenMate 3 месяца | 4 руб🖥":
        item_id = 6
        amount_from_balance = 4

    elif message.text == "GTA V | 3 руб💿":
        item_id = 7
        amount_from_balance = 3

    elif message.text == "Far Cry 6 | 4 руб💿":
        item_id = 8
        amount_from_balance = 4

    elif message.text == "Промокод на 250 рублей | 2 руб🥪":
        item_id = 9
        amount_from_balance = 2

    elif message.text == "Промокод на 500 рублей | 4 руб🥪":
        item_id = 10
        amount_from_balance = 4

    for item in items:
        if item.id == item_id:
            await message.answer_photo(
                photo=item.photo_link,
                caption=caption.format(
                    title=item.title,
                    description=item.description,
                    price=item.price),
                parse_mode=ParseMode.HTML)

    await message.answer("Выберите способ оплаты: ",
                         reply_markup=payment_method_keyboard)


@dp.message_handler(text="Снять с баланса💰")
async def buy_balance(message: types.Message):
    user_id = message.from_user.id
    balance = check_balance(user_id=user_id)
    print(balance)
    if balance >= amount_from_balance:
        db = sqlite3.connect("user_data.db")
        cursor = db.cursor()
        sqlite_select_query = f"""SELECT balance from userss WHERE name={user_id}"""
        cursor.execute(sqlite_select_query)
        cursor.execute(f"""UPDATE userss SET balance=balance-{amount_from_balance} WHERE name={user_id}""")
        db.commit()
        cursor.execute(sqlite_select_query)
        x = cursor.fetchall()
        print(x)
        await message.answer("Успешно оплачено."
                             "\nДанные товара:",
                             reply_markup=catalog)
    else:
        await message.answer("Недостаточно средств!")


@dp.message_handler(text="Оплатить QIWI🥝")
async def buy(message: types.Message, state: FSMContext):
    amount = 0
    for item in items:
        if item.id == item_id:
            amount = item.price

    payment = Payment(amount=amount)
    payment.create()

    await state.set_state("qiwi")
    await state.update_data(payment=payment)

    await message.answer("Оплата товара❗",
                         reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f"<b>📲Номер для оплаты:</b> {wallet_qiwi}"
                         f"\n<b>🗝Комментарий к оплате:</b> <code>{payment.id}</code>"
                         f"\n<b>💸Оплатить:</b> {amount:.2f} RUB",
                         parse_mode=ParseMode.HTML,
                         reply_markup=key_k)



@dp.callback_query_handler(text="cancel", state="qiwi")
async def cancel_payment(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Отменено❌")
    await call.message.answer("🗂Главное меню", reply_markup=menu)
    await state.finish()


@dp.message_handler(text="Отменить❌")
async def cancel_payment(message: types.Message):
    await message.answer("💡Выберите категорию", reply_markup=catalog)


@dp.callback_query_handler(text="paid", state="qiwi")
async def approve_payment(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    payment: Payment = data.get("payment")
    try:
        payment.check_payment()
    except NoPaymentFound:
        await call.message.answer("Транзакция не найдена❌")
        return
    except NotEnoughMoney:
        await call.message.answer("Оплаченная сумма меньше необходимой")
        return
    else:
        await call.message.answer(f"Успешно оплачено"
                                  f"\nВаш товар:"
                                  f"\nЛогин - "
                                  f"\nПароль - ")
    await call.message.delete_reply_markup()
    await state.finish()

