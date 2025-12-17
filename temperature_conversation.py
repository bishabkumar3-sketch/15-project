# temperature conversation program
unit = input("Enter temperature in celsius or fahrenheit (C/F): ").lower()
temp = float(input("Enter the temperture: "))

if unit == "c":
    temp = round((9 *temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}F")
elif unit == "f":
    temp = round((temp - 32) * 5/ 9, 1)
    print(f"The temperture in celsius is: {temp}C")
else:
    print(f"{unit} is an invaid unit of measurement")

