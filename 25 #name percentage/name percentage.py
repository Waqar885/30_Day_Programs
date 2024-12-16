from itertools import zip_longest

def check_vowel(name1, name2):
    vowel = ['a', 'e', 'i', 'o', 'u']
    matches = 0
    for char1, char2 in zip(name1, name2):
        if char1 in vowel or char1 == char2:
            matches += 1
    
    percentage_vowel = (matches / max(1, min(len(name1), len(name2)))) * 10  # Weighted out of 10%
    return percentage_vowel

def check_percent(name1, name2, vowel):
    name_1 = []
    name_2 = []

    matches = 0
    for nam1, nam2 in zip(name1, name2):
        if nam1 != ' ' and nam2 != ' ':
            name_1.append(nam1)
            name_2.append(nam2)
    
    for char1, char2 in zip_longest(name_1, name_2, fillvalue=""): 

        if char1 == char2 and char1:  # Ensure non-empty comparison
            matches += 1

    if len(name_1)>0:
        percentage_character = (matches/len(name1)) * 80
        percentage_length = (len(name_2)/len(name_1)) * 10
        percentage = percentage_character + percentage_length + vowel


    else:
        percentage = 0

    print(f'The name percent is: {percentage:.2f}%')

while True:
    choice = input('Enter 1 for compair name\n2 for exit: ')
    
    if choice == '1':
        name_1 = input('Enter long name first: ').strip().lower()
        name_2 = input('Enter second name: ').strip().lower()
        check_percent(name_1, name_2, check_vowel(name_1, name_2))
    
    elif choice == '2':
        break

    else:
        print('Error please enter between 1-2')