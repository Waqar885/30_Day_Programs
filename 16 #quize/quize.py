questions = [
["What is the output of the following code❓ \nprint('Hello' + str(2))", "Hello2", "TypeError", "Hello 2", "SyntaxError", 1],
["Which of the following is not a valid variable name in Python❓", "my_var", "my-var", "_var", "var1", 2],
["What will 5 // 2 evaluate to❓", "2.5", "2", "2.0", "3", 2],
["Which of the following is used to comment in Python❓", "# This is a comment", "<!-- This is a comment -->", "/* This is a comment */", "// This is a comment", 1],
["Which of the following statements is true about Python❓", "Python is a low-level language.", "Python is case-sensitive.", "Python variables must be declared before use.", "Python uses curly braces {} to delimit blocks of code.", 2],
["What does the len() function do❓", "Converts a string to lowercase.", "Returns the length of a string, list, or tuple.", "Returns the square root of a number.", "Returns the largest item in an iterable.", 2],
["Which of the following is used to read user input in Python❓", "read()", "input()", "get()", "fetch()", 2],
["What is the correct way to open a file data.txt for reading in Python❓", "file = open('data.txt', 'r')", "file = open('data.txt', 'read')", "file = open('data.txt')", "file = open('data.txt', 'w')", 1],
["What will the expression 3 < 4 and 5 < 6 evaluate to❓", "True", "False", "3", "4", 1],
["Which of the following is not a valid Python data type❓", "int", "float", "double", "str", 3],
["Which of the following is a mutable data type in Python❓", "Tuple", "List", "String", "Integer", 2],
["What does the continue statement do in a loop❓", "Ends the loop", "Skips the current iteration and continues with the next one", "Restarts the loop", "Exits the loop entirely", 2],
["Which keyword is used to define a function in Python❓", "def", "func", "function", "declare", 1],
["What will type(5.0) return in Python❓", "int", "float", "double", "str", 2],
["Which method is used to add an item to the end of a list in Python❓", "append()", "insert()", "extend()", "add()", 1],
["What is the output of 2 ** 3 in Python❓", "5", "6", "8", "9", 3],
["Which of the following operators is used to check if two values are equal in Python❓", "=", "==", "!=", "===", 2],
["Which of the following is a valid Python loop❓", "for", "while", "do-while", "repeat", 2],
["How do you create a dictionary in Python❓", "{}", "[]", "()", "<>", 1],
["What will the expression 4 > 3 > 2 return❓", "True", "False", "3", "SyntaxError", 1],
["Which function is used to convert a string to a list of characters in Python❓", "list()", "split()", "convert()", "join()", 1],
["Which of the following is the correct syntax to import a module in Python❓", "import module_name", "include module_name", "using module_name", "require module_name", 1],
["What is the output of the following code: \nprint(3 * 'Python ')❓", "Python Python Python", "Python3", "3Python", "Error", 1],
["How do you access the first element in a list named my_list in Python❓", "my_list[1]", "my_list[0]", "my_list[-1]", "my_list.first()", 2],
["Which of the following methods is used to remove an item from a list by its value in Python❓", "pop()", "remove()", "delete()", "discard()", 2],
["What does the len() function return when applied to a list in Python❓", "The length of the list", "The last element in the list", "The first element in the list", "The sum of elements in the list", 1],
["Which statement is used to handle exceptions in Python❓", "try-except", "catch", "handle", "trap", 1],
["What is the correct way to declare a class in Python❓", "class MyClass:", "MyClass class:", "declare class MyClass:", "class: MyClass", 1],
["How can you get a list of all keys in a dictionary named my_dict❓", "my_dict.keys()", "my_dict.values()", "my_dict.items()", "my_dict.get_keys()", 1],
["Which of the following is not a Python built-in data type❓", "list", "dictionary", "array", "tuple", 3]
]

print("Small Python Test 😉".center(50))
correct = 0
total = 30
for i in range(len(questions)):
    question = questions[i]
    print(f"Q{i+1}: {question[0]}")
    print(f"a. {question[1]}          b.{question[2]}")
    print(f"c. {question[3]}          d.{question[4]}")
    user_choice = input("Enter your choice between 1-4: ")
    try:
        if int(user_choice) == question[-1]:
            correct += 1
            print("Correct Answer 👍")
        else:
            answer = question[-1]
            print("Wrong Answer 👎 ")
            print(f"The correct answer is: {question[answer]}")
    except:
        print("Please only enter number between 1-4")

if correct >= 20:
    print("Congratulations 🎉")
    print(f"Your score is: {correct} out of {total}")
    print("You passed the test 🤗")

else:
    print(f"Your score is: {correct} out of {total}")
    print("You Failed 😔 ")