import time
my_time = int(input("Enter your time: "))
for i in reversed(range(0, my_time)):
    second = i % 60
    minute = int(i /60) % 60
    hour = int( i/3600)
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)
print("--time up--")

