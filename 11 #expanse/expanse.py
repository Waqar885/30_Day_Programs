def add_amount(amount):
    with open("30_Days/ Day 11/expanse.txt", 'r') as f:
            lines = f.readlines()
            updated_line = []
            balance_updated = False
            for line in lines:
                if "Total Balace left" in line:
                    balance_start = line.find("Total Balace left:") + len("Total Balace left: ")
                    cash = int(line[balance_start:])
                    total = amount + cash
                    new_line = (f"Total Balace left: {total}\n")
                    updated_line.append(new_line)
                    balance_start = True
                    print("Amount added")
                else:
                    updated_line.append(line)
            
            if balance_updated:
                updated_line.append(f"Total Balace left: {amount}\n")
            
            with open("30_Days/ Day 11/expanse.txt", "w") as f:
                f.writelines(updated_line)


def add_items(Date, item, price):
    with open("30_Days/ Day 11/expanse.txt", 'a') as f:
        f.write(f"[Date: {Date}], [Item: {item}, Price: {price}]\n")
        
    updated = False
    with open("30_Days/ Day 11/expanse.txt", 'r') as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            if "Total Balace left" in line:
                balance_start = line.find("Total Balace left:") + len("Total Balace left: ")
                cash = int(line[balance_start:].strip())
                total = cash - price
                lines[index] = f"Total Balace left: {total}\n"
                updated = True
        
    if updated:
        with open("30_Days/ Day 11/expanse.txt", "w") as f:
            f.writelines(lines)
        print("Expense added successfully")
    else:
        print("Process not successful")

def total_money():
    with open("30_Days/ Day 11/expanse.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "Total Balace left" in line:
                print(line)
                break
def show_all():
    with open("30_Days/ Day 11/expanse.txt", "r") as f:
        text = f.read()
        print(text)
    
while True:
    print("Enter 1 for Add Balance")
    print("Enter 2 for Add Expense")
    print("Enter 3 for to check balance left")
    print("Enter 4 to show all Expense")
    print("Enter 5 to exit")
    choice = input("Enter between 1-5: ")

    if choice == "1":
        n = int(input("Enter the amount: "))
        add_amount(n)

    elif choice == "2":
        day = input("Enter the date: ")
        month = input("Enter the month: ")
        year = input("Enter the year: ")
        items = int(input("How much item you want to add in this date: "))
        for i in range(items):
            item = input("Enter the expense item name: ")
            price = int(input("Enter the expense amount: "))
            date = f"{day}-{month}-{year}"
            add_items(date, item, price)


    elif choice == "3":
        total_money()

    elif choice == "4":
        show_all()
    
    elif choice == "5":
        break

    else:
        print("Error found. Please enter between 1-4.")