import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis sir. Please tell me how may I help you")
def takeCommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',578)
    server.ehlo()
    server.starttls()
    server.login('barenyamishra123@gmail.com','Barenya@2000')
    server.sendmail('barenyamishra123@gmail.com',to,content)
    server.close()

if __name__== "__main__":
    WishMe()
    while True:
        # if 1:
            query = takeCommand().lower()
             # logic for executing task based on query
            if 'wikipedia'in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in query: 
                webbrowser.open("youtube.com")
            elif 'open google' in query:
                webbrowser.open('google.com')
            elif 'open stackoverflow' in query:
                webbrowser.open('stackoverflow.com')
            elif 'play music' in query:
                music_dir = 'D:\\ Non Critical \\ Songs\\Favourite Songs2'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))
            elif 'the time' in query:
                strTime = datetime.datetime.now().starttime("%H:%M:%S")
                speak(f"sir, the time is {strTime}")
            elif 'email to Barenya' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "barenyamishra123@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend Barenya bhai. I am not able to send this email")    
            else:
                print("No query matched")
 