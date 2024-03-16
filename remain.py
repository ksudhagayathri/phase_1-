class Remain:
    def __init__(self):
        self.remaining_amount = 8000

    def atm(self):
        print("initial remaining amount in the ATM:", self.remaining_amount)

    def update_atm(self, amount):
        self.remaining_amount += amount
        print("Updated ATM Balance:", self.remaining_amount)
