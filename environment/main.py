import pyttsx3 
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import distutils

engine =pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)  #1 FEMALE VOICE 0 MALE VOICE


def listen(audio):
    engine.say(audio)
    engine.runAndWait()

def startquery():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        listen("Good Morning Dear")
    elif hour>=12 and hour<18:
        listen("Good Afternoon Dear")
    else:
        listen("Good Evening Dear")
    listen("How can I help You Dear ?")

def passquery():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearing to you .....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Fetching your voice......")
        query = r.recognize_google(audio, language='en-in')
        print(f" You Said:{query}\n")
    except Exception as e:
        print("I can't understand, can you tell me once again")
        return None
    return query


def Email(to,content):
    server=smtplib.SMTP("smtp.gmail.com",535)
    server.ehlo()
    server.starttls()
    server.login('yourmailid','yourpassword')
    server.sendmail('yourmailid',to,content)
    server.close()

if __name__=='__main__':
    startquery()
    while True:
        query=passquery().lower()
        if 'open wikipedia' in query:
            listen('searching wikipedia content.......')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            listen("According to wikipedia")
            print(results)
            listen(results)
        elif 'open notepad' in query:
            npath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'tell me the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            listen(strTime)
        elif 'open linkedin' in query:
            webbrowser.open("www.linkedin.com")
        elif 'email' in query:
            try:
                listen("Tell me the Message")
                content=passquery()
                to="sendermailID"
                Email(to,content)
                listen(f"Your Email has been sent to the {to} successfully")
            
            except Exception as e:
                print(e)
                listen("Email is not Sent")
            

