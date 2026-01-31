import random

secret = random.randint(1, 10)
guess = int(input("Doan so tu 1 den 10: "))

while guess != secret:
    if guess > secret:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Doan lai: "))

print("Correct")
