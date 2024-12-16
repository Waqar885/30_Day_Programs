import re
import random
import json

def save_responses():
    with open('30_Programs/ Programs 27/chatbot.json', 'w') as write:
        json.dump(responses, write, indent=4)

def load_responses():
    global responses
    try:
        with open('30_Programs/ Programs 27/chatbot.json', 'r') as read:
            responses = json.load(read)
    except FileNotFoundError:
        responses = {}

default_response = [
    "I'm not sure about that.",
    "Can you rephrase your question?",
    "I don’t have an answer for that, but I'm learning!",
]

def chat(question):
    user_input = question.lower()

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
        
    return random.choice(default_response)

def main():
    choice = input('Enter 1 to speak with the ChatBot, 2 for feed you chatBot\n -> ')

    if choice == '1':
        print("ChatBot: Hello! Ask me anything, or type 'bye' to exit.")
        while True:
            user_input = input('You: ')
            chat(user_input)

            if 'bye' in user_input:
                print("ChatBot: Goodbye! Have a great day!")
                break

            print('Chatbot:', chat(user_input))

    elif choice == '2':
        
        while True:
            end = input('enter 0 to exit otherwise press any key to continue -> ')
            
            if end == '0':
                break
            
            else:    
                question = input('Enter question you want to feed -> ')
                answer = input('Enter answer of this question -> ')
                
                responses[question] = answer
        
        save_responses()
        print("ChatBot: Responses saved successfully!")

    else:
        print('Invailed input enter between 1-2')

if __name__ == "__main__":
    load_responses()
    main()