import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
char = list(chars)
key = char.copy()
random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key  :{key}")

plain_text = input("Enter a message to encrytion: ")
cipher_text = ""
for letter in plain_text:
    index = char.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrytion message: {cipher_text}")

cipher_text = input("Enter a message to encrytion: ")
plain_text= ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += char[index]
print(f"cipher message: {cipher_text}")
print(f"original message: {plain_text}")
