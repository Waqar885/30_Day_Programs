import pywhatkit

def send_text_message():
    number = input('Enter number with code (e.g., +91, +92) -> ')
    msg = input('Enter message -> ')
    hour = int(input('Enter hour in 24-hour format -> '))
    minute = int(input('Enter minute (must be at least 2 minutes later) -> '))
    try:
        pywhatkit.sendwhatmsg(number, msg, hour, minute)
        print('Message sent successfully...')
    except Exception as e:
        print(f"An error occurred: {e}")

def send_group_message():
    group_id = input('Enter group ID -> ')
    msg = input('Enter message -> ')
    hour = int(input('Enter hour in 24-hour format -> '))
    minute = int(input('Enter minute (must be at least 2 minutes later) -> '))
    try:
        pywhatkit.sendwhatmsg_to_group(group_id, msg, hour, minute)
        print('Message sent successfully...')
    except Exception as e:
        print(f"An error occurred: {e}")

def play_youtube_video():
    video = input('Enter YouTube video name -> ')
    try:
        pywhatkit.playonyt(video)
        print("Playing...")
    except Exception as e:
        print(f"An error occurred: {e}")

def google_search():
    topic = input('Enter topic to search -> ')
    try:
        pywhatkit.search(topic)
        print("Searching...")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_info():
    topic = input('Enter topic -> ')
    lines = int(input('Enter number of lines -> '))
    try:
        pywhatkit.info(topic, lines=lines)
        print("Successfully retrieved information.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print('\nEnter 1 for WhatsApp options...')
        print('Enter 2 to play YouTube videos...')
        print('Enter 3 for Google search...')
        print('Enter 4 to get information on a topic...')
        print('Enter 5 to exit...')
        
        choice = input('-> ')

        if choice == '1':
            print('\nEnter 1 to send a text message...')
            print('Enter 2 to send a group message...')
            sub_choice = input('-> ')
            if sub_choice == '1':
                send_text_message()
            elif sub_choice == '2':
                send_group_message()
            else:
                print('Invalid choice, please enter 1 or 2.')

        elif choice == '2':
            play_youtube_video()

        elif choice == '3':
            google_search()

        elif choice == '4':
            get_info()

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print('Error: please enter a valid choice between 1 and 5.')

if __name__ == "__main__":
    main()