# TODO здесь писать код

def calculate_balances(N, K, transactions):
    balances = {i + 1: 0 for i in range(N)}

    for i in range(K):
        borrower, lender, amount = transactions[i]
        balances[borrower] -= amount
        balances[lender] += amount

    return balances

N = int(input("Кол-во друзей: "))
K = int(input("Долговых расписок: "))

transactions = []
for i in range(K):
    print(f"{i + 1} расписка")
    borrower = int(input("Кому: "))
    lender = int(input("От кого: "))
    amount = int(input("Сколько: "))
    transactions.append((borrower, lender, amount))

balances = calculate_balances(N, K, transactions)

print("Баланс друзей:")
for friend, balance in balances.items():
    print(f"{friend} : {balance}")