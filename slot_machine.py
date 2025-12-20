# A python slot machine
import random
def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        if row[0] == "🍉":
            return bet * 4
        if row[0] == "🍋":
            return bet * 8
        if row[0] == "🔔":
            return bet * 10
        if row[0] == "⭐":
            return bet * 20
    return 0

def main():
    balance = 100

    print("**************************")
    print("Welcome to python slot")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐ ")
    print("**************************")

    while balance > 0:
        print(f"your current balance is{balance}")

        bet = input("Enter your bet amount: ")
        if not bet.isdigit:
            print("the bet amount is numercial")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient fund")
            continue

        if bet <=0:
            print("the bet amount is must be greater than zero")
            continue
        balance -= bet

        row = spin_row()
        print(row)
        print("Spinning... \n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"you won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (y/n)").lower()

        if play_again != "y":
            break
    print("********************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("********************************************")

if __name__ == "__main__":
    main()