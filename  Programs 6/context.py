def add(name, email, number):
    f = open("contact.txt", 'a')
    txt = f.write(f"\n[ Name: {name} ], [Email: {email}], [Number: {number}]")
    f.close()
    print("contact added")

def remove(name):
      with open("contact.txt", 'r') as f:
          lines = f.readlines()
      with open("contact.txt", 'w') as f:
        namae_found = False
        for line in lines:
            if name not in line:
                f.write(line)
            else:
                namae_found = True
        if not namae_found:
            print(name, "is not available in contact")
        else:
            print(name, "is removed from contact")

def show():
    f = open("contact.txt", 'r')
    txt = f.read()
    print(txt)
    f.close()

def search(name):
    with open("contact.txt", 'r') as f:
        name_found = False
        lines = f.readlines()
    for line in lines:
        if name in line:
            print(line)
            name_found = True
    if not name_found:
        print(name, "is not availabe in contact")
        
def del_all():
    f = open("contact.txt", 'w')
    f.close()
    print("all contact deleted")
while True:
  choice = (input("Enter\n 1 for add contact\n 2 for all show contacts\n 3 for remove contact\n 4 for search contact\n 5 for delete all contact\n 6 for exit: "))

  if (choice == "1"):
      name = input("Enter the contact name:--> ").title()
      email = input("Enter the contact email:--> ")
      number = input("Enter the contact number:--> ")
      add(name, email, number)

  elif (choice == "2"):
      show()

  elif (choice == "3"):
      name = input("Enter the contact name:--> ").title()
      remove(name)

  elif (choice == "4"):
      name = input("Enter the contact name:--> ").title()
      search(name)

  elif (choice == "5"):
      del_all()

  elif (choice == "6"):
      break
  else:
      print("Only enter between 1-6")