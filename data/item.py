from dataclasses import dataclass


@dataclass
class Item:
    id: int
    title: str
    description: str
    price: int
    photo_link: str


Big_mac = Item(id=1,
               title="Биг мак",
               description="QR-код для получения товара за один рубль",
               price=4,
               photo_link="https://tc-tiara.ru/images/2019/12/makdonalds.jpg")


Potato_mac = Item(id=2,
               title="Картошка маленькая",
               description="QR-код для получения товара за один рубль",
               price=2,
               photo_link="https://tc-tiara.ru/images/2019/12/makdonalds.jpg")

Box_kfc = Item(id=3,
               title="Пати бокс",
               description="QR-код для получения товара за один рубль",
               price=3,
               photo_link="https://hrlike.ru/wp-content/uploads/2020/11/kfc_png53.png")


Burger_kfc = Item(id=4,
               title="Чизбургер",
               description="QR-код для получения товара за один рубль",
               price=2,
               photo_link="https://hrlike.ru/wp-content/uploads/2020/11/kfc_png53.png")

Nord_vpn = Item(id=5,
               title="Nord VPN 365 дней",
               description="Аккаунт в формате Логин/Пароль",
               price=3,
               photo_link="https://www.digiseller.ru/preview/496886/p1_3028064_a35877c5.jpg")

Zen_vpn = Item(id=6,
               title="ZenMate 3 месяца",
               description="Аккаунт в формате Логин/Пароль",
               price=4,
               photo_link="https://www.husham.com/wp-content/uploads/2020/04/1588178788_ZenMate-VPN-"
                          "Review-2020-%E2%80%93-Fast-Evolving-VPN-Service-That-Still.png")

Gta_games = Item(id=7,
               title="GTA V",
               description="Аккаунт в формате Логин/Пароль",
               price=3,
               photo_link="https://i.playground.ru/p/7BsZf78hIXpABUTSpoLyKQ.png")

Farcry_games = Item(id=8,
               title="Far Cry 6",
               description="Аккаунт в формате Логин/Пароль",
               price=4,
               photo_link="https://www.playscope.com/wp-content/uploads/2020/07/farcry6_forwardimages_0003-scaled.jpg")

Yandex_promo250 = Item(id=9,
               title="Промокод на 250 рублей",
               description="Промокод актвируется при оплате заказа",
               price=2,
               photo_link="https://geekville.ru/wp-content/uploads/2018/08/yandex-logo-1600x900.jpg")

Yandex_promo500 = Item(id=10,
               title="Промокод на 500 рублей",
               description="Промокод актвируется при оплате заказа",
               price=4,
               photo_link="https://geekville.ru/wp-content/uploads/2018/08/yandex-logo-1600x900.jpg")


items = [Big_mac, Potato_mac, Box_kfc, Burger_kfc, Nord_vpn, Zen_vpn, Gta_games, Farcry_games, Yandex_promo250,
         Yandex_promo500]
