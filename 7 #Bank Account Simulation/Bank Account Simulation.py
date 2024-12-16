def deposit(cash, deposit_amount):                                        
    cash += deposit_amount
    return cash

def withdraw(cash, amount):    
    if amount <= cash:
        cash -= amount
        print("withdraw successfull. your current balance is: ", cash)
    else:
        print("Your withdrawal value is greater than your current ammount. Try again")
    return cash

bank_name = "Bank Account Simulation"
print(bank_name.center(50))

info = input("Enter\n 1 to create new account \n 2 if you already have account: ")
if (info == "1"):
    name = input("Enter your full name: ").title().strip()
    phone = input("Enter your phone number: ").strip()
    pin = input("Set PIN: ").strip()

    with open("30_Days/ Day 7/Account detail.txt", 'a') as f:
        f.write(f"\n[Name: {name}, PIN: {pin}, Phone Number: {phone}, Balance: 0]")
    print("You account has been created")


elif (info == "2"):
    name = input("Enter your account name: ").title().strip()
    password = input("Enter your PIN: ").strip()
    phone = input("Enter your phone no: ").strip()

    found = False
    cash = 0
    with open("30_Days/ Day 7/Account detail.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            if name in line and password in line and phone in line:
                found = True
                balance_start = line.find("Balance:") + len("Balance: ")
                cash = int(line[balance_start:].strip("]\n"))
                break
    if found:
        
        while True:
            print("Enter\n 1 for Deposit\n 2 for withdraw \n 3 for check balance\n 4 for exit")
            detail = input("Enter your choice: ")
            if (detail == "1"):
                        deposit_amount = int(input("Enter amount range you want to deposite: "))
                        cash = deposit(cash, deposit_amount)
                        print("Deposit successfully.Your current balance is: ", cash)   
                            
            elif (detail == "2"):
                withdraw_amount = int(input("Enter amount range you want to withdraw: "))    
                cash = withdraw(cash, withdraw_amount)
                                
            elif (detail == "3"):
                print("Your current balance is: ", cash)
            elif (detail == "4"):
                with open("30_Days/ Day 7/Account detail.txt", 'w') as f:
                    for line in lines:
                        if name in line and password in line:
                            line = f"[Name: {name}, PIN: {password}, Phone Number: {phone} Balance: {cash}]"
                            f.write(line)
                break
            else:
                print("Invalid choice. Please enter between 1-4")
    else:
        print("Invalid Name or PIN. Please enter a valid Name or PIN")
else:
    print("Invalid choice. Please enter 1 or 2")            