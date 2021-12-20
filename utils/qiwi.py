import datetime
from dataclasses import dataclass
import uuid
import pyqiwi
from data.config import qiwi_wallet, wallet_qiwi

wallet = pyqiwi.Wallet(token=qiwi_wallet, number=wallet_qiwi)


class NotEnoughMoney(Exception):
    pass


class NoPaymentFound(Exception):
    pass


@dataclass
class Payment:
    amount: int
    id: str = None

    def create(self):
        self.id = str(uuid.uuid4())
        self.id = self.id[-12:]
        print(self.id)

    def check_payment(self):
        start_date = datetime.datetime.now() - datetime.timedelta(days=2)
        transactions = wallet.history(start_date=start_date).get("transactions")
        for transactions in transactions:
            if transactions.comment:
                if str(self.id) in transactions.comment:
                    if float(transactions.total.amount) >= float(self.amount):
                        return True
                    else:
                        raise NotEnoughMoney
        else:
            raise NoPaymentFound


@property
def invo(self):
    link = "https://oplata.qiwi.com/create?publicKey={pubkey}&amount={amount}&comment={comment}"
    qiwi_pub = "48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3" \
               "BGPiMsyXQFNKQhvukniQG8RTVhYm3iPsxfkgBCAZxuoo" \
               "hh51KQWKgMJdVXUgA7kZgGmrRA6k3GVAtgvhHEXXNE3Cj4Hv" \
               "D2SK6E57PchnKKmMxCYDpTQbNv2ScYu7ZSBZEqhoCMRg"
    print(link.format(pubkey=qiwi_pub, amount=self.amount, comment=self.id))
    return link.format(pubkey=qiwi_pub, amount=self.amount, comment=self.id)






