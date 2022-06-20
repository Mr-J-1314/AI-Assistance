import code
from importlib.resources import path
from re import M
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now( ).hour)

    if hour>=0 and hour<12:
        speak("Good Morning Sir..!")

    elif hour<=12 and hour>18:
        speak("Good Afternoon Sir..!")

    else:
        speak("Good Evening Sir..!")
        
    speak("I am AI. How may i help you?")  


    # it takes microphone input from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return 'None'
        
    return query 

if __name__ == "__main__":
    wishMe()
# while True:
if 1:    
    query = takeCommand().lower()

    # logic for executing tasks on query.
    if 'wikipedia' in query:
        speak('Searching Wikipedia')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        
    elif 'open google' in query:
        webbrowser.open("google.com")
    
    # elif 'open stackoverflow' in query:
        # webbrowser.open("stackoverflow.com")
    
    elif 'open whatsapp web' in query:
        webbrowser.open("https://web.whatsapp.com/") 

    elif 'open git' in query:
        webbrowser.open("github.com")

    elif 'play music' in query:
        music_dir =  'C:\\Users\\Laxmi\\Desktop\\jatin\\.mp3'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        
    # elif 'the time' in query:
    #     strTime = datetime.timedelta().now().strfTime("%H:%M:&S")
    #     speak(f"Sir, the time is{strTime}")

    elif 'open vs code' in query:
        codepath = "C:\\Users\\Laxmi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)



