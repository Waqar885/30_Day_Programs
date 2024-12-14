import random

x = random.randrange(1, 20)
y = random.randrange(1, 40)
z = random.randrange(1, 60)

print("Enter 1 for 1-20 number guess in 5 attempts")
print("Enter 2 for 1-40 number guess in 5 attempts")
print("Enter 3 for 1-60 number guess in 5 attempts")

choice = input("Enter the number 1-3: ")
try:
    if (choice == "1"):
        i = 0
        while (i < 5):
            a = int(input("Guess the from 1-20: "))
            if (a < x):
                print(f"Enter greater number than {a}")
            elif(a > x):
                print(f"Enter less number than {a}")
            elif (a == x):
                print(f"Yes you win the number is {x}")
                break
            i = i+1
        print(f"The number is {x}")
    elif (choice == "2"):
        i = 0
        while (i < 5):
            a = int(input("Guess the from 1-40: "))
            if (a < y):
                print(f"Enter greater number than {a}")
            elif(a > y):
                print(f"Enter less number than {a}")
            elif (a == y):
                print(f"Yes you win the number is {y}")
                break
            i = i+1
        print(f"The number is {y}")
    elif (choice == "3"):
        i = 0
        while (i < 5):
            a = int(input("Guess the from 1-60: "))
            if (a < z):
                print(f"Enter greater number than {a}")
            elif(a > z):
                print(f"Enter less number than {a}")
            elif (a == z):
                print(f"Yes you win the number is {z}")
                break
            i = i+1
        print(f"The number is {z}")
except:
    print("Invalid input only enter number! Try Again")