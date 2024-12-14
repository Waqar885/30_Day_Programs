import random
while True:
    player_choice = input("Enter 0 for exit \n 'a' for Rock\n 'b' for Scissor\n 'c' for Paper:\n")
    while (player_choice != "a" and player_choice != "b" and player_choice != "c" and player_choice!= "0" ):
        player_choice = input("Only enter 'a' for Snake\n 'b' for Water\n 'c' for Gun\n and 0 for exit:\n")

    a = "Rock"
    b = "Scissor"
    c = "Paper"
    if (player_choice == "0"):
        print("Game is closed")
        break
    if (player_choice == "a"):
        print(f"Your choice is: {a}")
    if (player_choice == "b"):
        print(f"Your choice is: {b}")
    if (player_choice == "c"):
        print(f"Your choice is: {c}")
    random_choice = (a, b, c)
    computer = random.choice(random_choice)
    print(f"Computer choice is: {computer}")

    if(player_choice == "a" and computer == b):
        print("You win")
    elif(player_choice == "a" and computer == c):
        print("you loss")
    if (player_choice == "b" and computer == a):
        print("you loss")
    elif(player_choice == "b" and computer == c):
        print("You win")
    elif(player_choice == "c" and computer == a):
        print("You win")
    elif(player_choice == "c" and computer == b):
        print ("you loss")
    else:
        print("Game is Draw")