from loader import dp
from aiogram import types
from aiogram.types import ParseMode, CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from utils import Payment, NotEnoughMoney, NoPaymentFound
from keyboards.inline.buy_menu import key_pay_balance
import sqlite3
import uuid
from data.config import qiwi_wallet, wallet_qiwi
import pyqiwi
import datetime

wallet = pyqiwi.Wallet(token=qiwi_wallet, number=wallet_qiwi)


class Form(StatesGroup):
    name = State()


user_id = ""
amount = 0
id = ""


def create():
    global id
    id = str(uuid.uuid4())
    id = id[-12:]
    print(id)


def check_payment(amount):
    start_date = datetime.datetime.now() - datetime.timedelta(days=2)
    transactions = wallet.history(start_date=start_date).get("transactions")
    for transactions in transactions:
        if transactions.comment:
            if str(id) in transactions.comment:
                if float(transactions.total.amount) >= float(amount):
                    return True
                else:
                    raise NotEnoughMoney
    else:
        raise NoPaymentFound


def put_money(amount):
    db = sqlite3.connect("user_data.db")
    cursor = db.cursor()
    sqlite_select_query = f"""SELECT * from userss WHERE name={user_id}"""
    cursor.execute(sqlite_select_query)
    cursor.execute(f"""UPDATE userss SET balance=balance+{amount} WHERE name={user_id}""")
    db.commit()
    cursor.execute(sqlite_select_query)
    x = cursor.fetchall()
    print(x)


@dp.message_handler(text="Пополение QIWI🥝")
async def pay_qiwi(message: types.Message):
    global user_id
    user_id = str(message.from_user.id)
    await Form.name.set()
    await message.answer("❕Введите сумму платежа, чтобы создать заявку на пополнение"
                         "\n❗Максимальная сумма пополнения от 1 руб до 1000",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=Form.name)
async def process(message: types.Message, state: FSMContext):
    global amount
    async with state.proxy() as datas:
        datas["name"] = message.text
        count_pay = datas["name"]

        try:
            int(count_pay)
            if 0 < int(count_pay) <= 1000:
                await state.finish()
                amount = count_pay
                print(amount)
                create()
                await state.set_state("qiwi")
                await state.update_data(payment=amount)
                print(count_pay)
                await message.answer(f"<b>📲Номер для оплаты:</b> +79297918555"
                                     f"\n<b>🗝Комментарий к оплате:</b>: <code>{id}</code>"
                                     f"\n<b>💸Оплатить:</b> {amount} RUB",
                                     parse_mode=ParseMode.HTML,
                                     reply_markup=key_pay_balance)

            else:
                await message.answer("Введите сумму от 1 до 1000")

        except ValueError:
            await message.answer("Введите число!")



@dp.callback_query_handler(text="paid_balance", state="qiwi")
async def approve_payment(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    payment: Payment = data.get("name")
    print(payment)
    try:
        check_payment(amount=amount)
        put_money(payment)

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

