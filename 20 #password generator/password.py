import random

def Generate_password():
    account_name = input("Enter name as you want to save password: ").capitalize()
    speacial_character = '!', '@', '#', "$", '%', "^", "&", "*", "(", ")", "-", "_", "=", "+", "|", ";"
    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    number = "1", "2", "3", "4", "5", "6", "7", "8", "9"
    
    password = []

    while len(password) < 12:
        password.append(random.choice(alphabet).upper())
        password.append(random.choice(alphabet).lower())
        password.append(random.choice(speacial_character))
        password.append(random.choice(number))
    
    with open('30_Programs/ Programs 20/Accounts.txt', 'a') as account:
        account.write(f"{account_name}: {''.join(password)}\n")

    print("Your password been saved")
    print(f"The {account_name} password is:", ''.join(password))

def find_password(name):
    with open('30_Programs/ Programs 20/Accounts.txt', 'r') as search:
        lines = search.readlines()
    found = True
    for line in lines:
        if name in line:
            print(line)
            break
        else:
            found = False
    if not found:
        print("Account is not available")

while True:
    choice = input("Enter 1 for generate new password \n2 for find password\n3 for exit: ")

    if choice == "1":
        Generate_password()

    elif choice == "2":
        name = input("Enter account name you saved password: ").capitalize()
        find_password(name)

    elif choice == "3":
        break
    else:
        print("Error: Only enter between 1-3")