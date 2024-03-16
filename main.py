from login import Card
from remain import Remain

def main():
    obj1= Remain()
    obj1.atm()
    obj = Card(obj1)
    obj.types()
    
    while True:
        print("\nEnter an option:")
        print("1. Check Balance")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Mini Statement")
        print("5. Exit")
        
        choice = int(input())
        
        if choice == 1:
            obj.check_balance()
        elif choice == 2:
            obj.cash_withdrawal()
        elif choice == 3:
            obj.cash_deposit()
        elif choice == 4:
            obj.mini_statement()
        elif choice == 5:
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

main()



