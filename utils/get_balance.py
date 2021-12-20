import uuid
import sqlite3
import datetime
from data.config import qiwi_wallet, wallet_qiwi
from utils import NotEnoughMoney, NoPaymentFound
import pyqiwi

# wallet = pyqiwi.Wallet(token=qiwi_wallet, number=wallet_qiwi)
#
#
# class user_balance:
#     id_balance: str
#     amount: int
#
#     def get_pay_id(self):
#         self.id_balance = str(uuid.uuid4())
#         self.id_balance = self.id_balance[-12:]
#         print(self.id_balance)
#
#     def check_pay_balance(self):
#         start_date = datetime.datetime.now() - datetime.timedelta(days=2)
#         transactions = wallet.history(start_date=start_date).get("transactions")
#         for transactions in transactions:
#             if transactions.comment:
#                 if str(self.id_balance) in transactions.comment:
#                     if float(transactions.total.amount) >= float(self.amount):
#                         return True
#                     else:
#                         raise NotEnoughMoney
#         else:
#             raise NoPaymentFound


def check_balance(user_id):
    db = sqlite3.connect("user_data.db")
    cursor = db.cursor()
    cursor.execute(f"""SELECT * from userss WHERE name={user_id}""")
    show_all = cursor.fetchall()
    print(show_all)
    for i in show_all:
        balance = i[1]
        return balance
