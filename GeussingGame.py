import random

ranNum = random.randint(1, 100)

while True:
    Number = int(input("Enter a number: "))
    if Number > ranNum:
        print("Too high")
    elif Number < ranNum:
        print("Too low")
    else:
        print("Correct")
        break

