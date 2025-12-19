def show_balance(balance):
    print(f"your balance is:{balance:.2f}")
    


def deposit():
    amount = float(input("Enter your amount to deposit:$  "))

    if amount <=0:
        print("this is not a valid amount")
        return 0
    else:
        return amount

def withdraws(balance):
    amount = float(input("Enter your withdaws amount: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount <=0:
        print("the amount is not zero or negative")
        return 0
    else:
        return amount
def main():
    balance =0

    while True:
        print("*************************")
        print("   the banking program   ")
        print("*************************")
        print("1. show balance")
        print("2. deposit")
        print("3. withdraws")
        print("4. exit")

        choice = input("Enter in chioce(1 to 4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraws(balance)
        elif choice == "4":
            break 
        else:
            print("this is invalid choice")
            
print("thank you!")

if __name__ == "__main__":
    main()