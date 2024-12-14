while True:
    message = input("Enter Message: ")
    choice = input("Enter 1 for coding and 2 for Decode and 3 to exit: ")

    if choice == "1":
        coded = []
        for i in message:
            num = ord(i)
            if i != " ":
                if i == "X" or i == "Y" or i == "Z":
                    num = ord(i) - 23

                elif i == "x" or i == "y" or i == "z":
                    num = ord(i) - 23

                else:
                    num += 3
            coded.append(chr(num))
            
        print("".join(coded))


    elif choice == "2":
        decoded = []
        for i in message:
            num = ord(i)
            if i != " ":
                if i == "A" or i == "B" or i == "C":
                    num = ord(i) + 23

                elif i == "a" or i == "b" or i == "c":
                    num = ord(i) + 23

                else:
                    num -= 3
            decoded.append(chr(num))

        print("".join(decoded))
    
    elif choice == "3":
        break

    else:
        print("Please enter between 1-3")