# By Project Umang Modi

import pyttsx3
import datetime
import speech_recognition as sr
import aifc
import audioop
import wikipedia
import webbrowser
import os
import smtplib

data = pyttsx3.init("sapi5")
voice = data.getProperty("voice")

def Speak(audio):
    data.say(audio)
    data.runAndWait()
def date_time():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        print("Good Morning")
    elif hour >= 12 and hour < 18:
        print("Good Afernoon")
    else:
        print("Good Evening")

    Speak("I am Robot ? Please tell me how i help you ?")

def takeUservoice():
    # It Takes Microphones input from user and returns string Output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Jarvis")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing.....")
            query = r.recognize_bing(audio, Language="en-in")
            print(f"User Said : {query}\n")

        except Exception as e:
            print("Say that again please...")
        return "None"
    return query

def SendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("Umangmodi003@gmail.com","Umang@9313")
    server.sendmail("Umangmodi003@gmail.com",to,content)
    server.close()


if __name__ == "__main__":
    date_time()
    if 1:
        query = takeUservoice().lower()

    # Coding logic of Jarvis
        if 'wikipedia' in query:
            Speak("Searching Wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            Speak("Accroding to Wikipedia")
            print(results)
            Speak(results)

        elif 'open_browser' in query:
            webbrowser.open("youtube.com")

        elif 'open_google' in query:
            webbrowser.open("google.com")

        elif 'open_stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        # elif 'play_music' in query:

        elif 'the_time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, The Current Time is : {strTime} ")

        elif 'email to Umang' in query:
            try:
                print("What should I Say ? ")
                content = takeUservoice()
                to = "Umangmodi003@gmail.com"
                SendEmail(to, content)
                Speak("Email has been sent!")

            except Exception as e:
                print(e)
                print("Sorry! Umang. I am not able to send this Email.")

        elif 'quit' in query:
            exit()





