import speech_recognition as sr
import win32com.client as win
import webbrowser, re
import json, wikipedia

def say(text):
    speak = win.Dispatch("Sapi.spvoice")
    speak.speak(text)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language="en-pa")
            print(f"User said: {query}")
            return query.lower()
        
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            say("I could not understand the audio")
            

        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            say("Request error with Google Speech Recognition service")
        return None

def get_responses():
    global responses
    try:
        with open('30_Programs/ Programs 27/chatbot.json', 'r') as read:
            responses = json.load(read)
    except FileNotFoundError:
        responses = {}
    global sites
    try:
        with open('30_Programs/ Programs 30/Websites.json', 'r') as site:
            sites = json.load(site)
    except FileNotFoundError:
        sites = {}

def info(query):
    try:
        summary = wikipedia.summary(query, sentences=2)  # Fetch 2 sentences
        print("Note: It is taken from wikipedia...")
        say(summary)

    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation Error:", e.options)
        say(e.options)
    except wikipedia.exceptions.PageError:
        print("Page not found.")
        say("Page not found.")

def main():
    while True:
        text = takecommand()
            
        if not text:
            continue

        found = False
        for site_name, site_url in sites.items():
                if f'Open {site_name}'.lower() in text:
                    say(f'Opening {site_name} Sir...')
                    found = True
                    webbrowser.open(site_url)

        if 'bye assistant' in text:
            say('Googbye sir have a nice day.')
            break

        for pattern, response in responses.items():
            if re.search(pattern, text):
                say(response)
                found = True

        if text and not found:
            info(text)



if __name__ == "__main__":
    get_responses()
    main()