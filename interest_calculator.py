# interest calculator program 

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter your principle: "))

    if principle <=0:
        print("the value of principle not zero or negative")
        
    
while rate <= 0:
    rate = float(input("Enter your rate: "))

    if rate <=0:
        print("the value of rate not zero or negative")
        break
while time <= 0:
    time = int(input("Enter your time: "))

    if time <=0:
        print("the value of time not zero or negative")
        break

total_amount = principle * pow(1+rate /100, time)

print(total_amount)