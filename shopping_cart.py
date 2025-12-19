# shopping cart program 

foods = []
prices = []
total = 0

while True:
    food  = input("Enter your food item or (q to quit): ").lower()

    if food == "q":
        break
    else:
        price = float(input(f"Enter your price of {food}:$ "))

        foods.append(food)
        prices.append(price)

print("---your cart---")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"the total prices is: ${total}")