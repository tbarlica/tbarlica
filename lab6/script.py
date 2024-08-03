class CashRegister:
    def __init__(self, balance, name):
        self.balance = balance
        self.transactions = []
        self.name = name

    def add_transaction(self, amt):
        self.transactions.append(amt)
        self.balance = sum(self.transactions)

    def __add__(self, amt):
        self.add_transaction(amt)
        return self

    def __lt__(self, amt):
        return self.balance < amt

    def __str__(self):
        return f"Today's balance: $ {self.balance:.2f}"

    def __repr__(self):
        return f"{self.name}'s cash register with {len(self.transactions)} transactions"

#testing
if __name__ == "__main__":
    c1 = CashRegister(0.00, 'Chris')
    c1 + 2.00
    c1 + 3.00
    print(c1.transactions)
    print(c1.name)
    print(c1)
    print(c1 < 10.0)
    print(c1 < 1.0)
    print(repr(c1))