# What can this A.I. desktop assistant do for you?
# It can send emails on your behalf.
# It can play music for you.
# It can do Wikipedia searches for you.
# It is capable of opening websites like Google, Youtube, etc., in a web browser.
# It is capable of search on google
# It can also search on youtube
# It is capable of opening your code editor or IDE with a single voice command.
# It is capable of open notepad
# It can capable of take note
# It can tell jokes
# It can open calculator


import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes

engine = pyttsx3.init('sapi5')  # sapi5 is microsoft inbuilt voice tool
voices = engine.getProperty('voices')  # getting details of current voice
# print(voices[0].id)    #for change the value to get a new voice assistant
engine.setProperty('voice', voices[0].id)


def speak(audio):

    #    pass      #For now, we will write the conditions later.
    engine.say(audio)

    # Without this command, speech will not be audible to us.
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Albij Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # from google app password option create device password,,,from security option
    server.login('b190305008@cse.jnu.ac.bd', 'kchzpfkpgyvltvfr')
    server.sendmail('b190305008@cse.jnu.ac.bd', to, content)
    server.close()


def tellJoke():
    joke = pyjokes.get_joke()
    speak(joke)
    print(joke)


def takeNote():
    speak("What would you like to note?")
    note = takeCommand()
    with open("notes.txt", "a") as file:
        file.write(f"{datetime.datetime.now()}: {note}\n")
    speak("Note has been saved.")


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":

    wishMe()
while True:
# if 1:
    query = takeCommand().lower()
    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'search on youtube' in query:  
        speak("What would you like to search on YouTube?")
        search_query = takeCommand()
        webbrowser.open(
            f"https://www.youtube.com/results?search_query={search_query}")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'search on google' in query:
        speak("What should I search on Google?")
        search_query = takeCommand()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'open facebook' in query:
        webbrowser.open("facebook.com")
    elif 'take a note' in query:
        takeNote()
    elif 'play music' in query:
        music_dir = 'C:\\Users\\USER\\Music\\favourite'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'tell me a joke' in query:
        tellJoke()

    elif 'open code' in query:
        codePath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    elif 'open notepad' in query:
        os.system('notepad')

    elif 'open calculator' in query:
        os.system('calc')
    elif 'email to raihan' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "raihanabdurrahman68@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry my friend Raihan bhai. I am not able to send this email")
