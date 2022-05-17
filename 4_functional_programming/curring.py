from functools import partial

# Каррирование (от Англ. curring, иногда - карринг) - преобразование функции от многих аргументов в набор функций,
# каждая из которых является функцией от одного аргумента. По факту же просто от меньшего числа аргументов.

def money_transfer(client_from, client_to, amount, currency, pay_system):
    print(f"Transfer from: {client_from} to {client_to} made for {amount} {currency} with {pay_system}")
    
    
rub_money_transfer = partial(money_transfer, currency="RUB", pay_system="UnionPay")
eur_money_transfer = partial(money_transfer, currency="EUR", pay_system="VISA")
usd_money_transfer = partial(money_transfer, currency="USD", pay_system="MasterCard")

if __name__ == "__main__":
    rub_money_transfer("Maksim", "Nina", 30000)
    eur_money_transfer("Kolya", "Lesha", 300)
    usd_money_transfer("Pasha", "Maksim", 300)
