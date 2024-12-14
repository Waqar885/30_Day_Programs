man = ['''
   |-----------
   |        
   |
   |
   |
   |
''',
'''
   |-----------
   |        |
   |
   |
   |
   |
''',
'''
   |-----------
   |        |
   |        O
   |
   |
   |
''',
'''
   |-----------
   |        |
   |        O
   |        |
   |
   |
''',
'''
   |-----------
   |       | 
   |       O
   |       |\\
   |
   |
''',
'''
   |-----------
   |       | 
   |       O
   |      /|\\
   |
   |
''',
'''
   |-----------
   |        |
   |        O
   |       /|\\
   |       /
   |
''',

'''
   |-----------
   |        |
   |        O
   |       /|\\
   |       / \\
   |
'''
]
for i in range(len(man)):
    subm = man[i]
import random
import os

with open("30_Days/ Day 8/words", 'r') as file:
   word = file.read()

word_split = word.split(", ")
words = random.choice(word_split)
ran = words

Guessed = "_" * len(ran)

incorrect = set()

attempts = 7



while attempts > 0 and "_" in Guessed:
   os.system('cls')
   print(man[8 - attempts])
   print(" ".join(Guessed))
   print(f"Your left attempt is: {attempts}")
   print(f"Incorrect guesses: {", ".join(incorrect)}")
   guess = input("Enter letter: ").lower()
   if guess in ran:
      for x in range(len(ran)):
        if ran[x] == guess:
            Guessed = Guessed[:x] + guess + Guessed[x+1:]

   else:
      if guess not in incorrect:
         attempts -= 1
         incorrect.add(guess)
   # print(" ".join(Guessed))
   

if "_" not in Guessed:
    print("Congratulation, You win")
else:
    print(f"Ohh! You loss the word was: {ran}")