sum_of_odd =  0
sum_of_even = 0
total = 0

card_num = input("Enter your number: ")
card_num = card_num.replace("-","")
card_num = card_num.replace(" ","")
card_num = card_num[::-1]

for i in card_num[::2]:
    sum_of_odd += int(i)

for i in card_num[1::2]:
    i = int(i) * 2
    if i >= 10:
        sum_of_even +=(1+ (i % 10))
    else:
        sum_of_even += i

total = sum_of_even + sum_of_odd

if total % 10 == 0:
    print("Valid")
else:
    print("Not Invalid")
