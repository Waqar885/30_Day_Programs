def main_menu():
    heading  = "Shopping List Menu"
    headingcapital = heading.upper()
    print(headingcapital.center(50))
    print("1. View shopping list ")
    print("2. Add item to shopping list ")
    print("3. Remove item from shopping list ")
    print("4. Exit ")

def shopping_list(shop_list):
    if not shop_list:
        print("The shopping list is empty.")
    else:
        print("The shopping list is: ")
        for item, i in enumerate(shop_list, 1):
            print(f"{item}. {i}")

def add_item(shoping_item):
    print("ITEM".center(50))
    items = [
        ("Laptop", 1200),
        ("Phone", 800),
        ("Headphones", 150),
        ("Keyboard", 100),
        ("Mouse", 50),
        ("Speaker", 75),
        ("Monitor", 450),
    ]
    for item, price in items:
        print(f"-> {item}: ${price}")
    loweritems = [item.lower() for item, price in items]
    add = input("Enter item name: ").lower()
    if add in loweritems:
        shoping_item.append(add)
        print(f"The {add.capitalize()} is added to the shopping list")
    else:
        print("Item is not available")
def price_check(shoping_item):
    items = [
        ("Laptop", 1200),
        ("Phone", 800),
        ("Headphones", 150),
        ("Keyboard", 100),
        ("Mouse", 50),
        ("Speaker", 75),
        ("Monitor", 450),
    ]
    
    loweritems = {item.lower(): price for item, price in items}
    total_price = 0
    
    # Convert all items in the shopping list to lowercase
    shoping_item = [item.lower() for item in shoping_item]
    
    for item in shoping_item:
        if item in loweritems:
            total_price += loweritems[item]
    
    print(f"The total price is ${total_price}")

def remove_item(remove_list):
    remove = input("Enter item name which you want to remove: ").lower()
    for item in remove_list:
        small_li = item.lower()
    if remove in item:
        remove_list.remove(remove)
        print(remove_list)
    else:
        print("Item is not in list")
        

lists = []
running = True
while running:
    main_menu()
    choice = input("Enter your choice 1-4: ")
    try:
        if (choice == "1"):
            shopping_list(lists)
        elif (choice == "2"):
            add_item(lists)
        elif (choice == "3"):
            remove_item(lists)
        elif (choice == "4"):
            running = False
            print("The item list is:")
            for itm in lists:
                print(f"-> {itm.capitalize()}")
            price_check(lists)
            break
        else:
            print("Invalid number only between 1-4")
    except:
        print("Please enter only number between 1-4")
    
