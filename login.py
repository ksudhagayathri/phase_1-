class Card:
    def __init__(self, remain_instance):
        self.main_balance=5000
        self.card_amount = 0
        self.transactions = []
        self.remain_instance = remain_instance

    def types(self):
        while True:
            print("Enter the type of card you want to use:\n1.Rupay card\n2.Visa card\n3.Master card")
            n1 = int(input())
            if n1 == 1:
                self.card_amount = 2000
                print("Thanks for selecting Rupay card")
                break
            elif n1 == 2:
                self.card_amount = 5000
                print("Thanks for selecting Visa card")
                break
            elif n1 == 3:
                self.card_amount = 8499
                print("Thanks for selecting Master card")
                break
            else:
                print("Enter valid card type")

    def check_balance(self):
        print("Balance:", self.card_amount)

    def cash_withdrawal(self):
        while True:
            print("Enter the amount of cash you need to withdraw:")
            withdraw = int(input())
            if self.card_amount >= withdraw:
                self.main_balance-=withdraw
                self.transactions.append(f"Withdrawal: -{withdraw}")
                print("Balance:", self.main_balance)
                self.remain_instance.update_atm(-withdraw)
                break
            else:
                print("Withdrawal amount exceeds ATM limit")

    def cash_deposit(self):
        while True:
            print("Enter the amount of cash you need to deposit:")
            deposit = int(input())
            self.main_balance+= deposit
            self.transactions.append(f"Deposit: +{deposit}")
            print("Balance:", self.main_balance)
            self.remain_instance.update_atm(+deposit)
            break

    def mini_statement(self):
        print("Mini Statement:")
        if len(self.transactions) == 0:
            print("No transactions yet.")
        else:
            for i in range(max(0, len(self.transactions) - 3), len(self.transactions)):
                print(self.transactions[i])

