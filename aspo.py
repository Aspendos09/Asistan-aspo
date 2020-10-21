
import datetime

import os
import time
import subprocess
from core import speak 
from core import takeCommand
from web import search_web


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=5 and hour<12:
        speak("Günaydın",1)
        print("Günaydın")
    elif hour>=12 and hour<18:
        speak("İyi Günler",1)
        print("İyi Günler")
    elif hour>=18 and hour<22:
        speak("İyi Akşamlar",1)
        print("İyi Akşamlar")
    else:
        speak("İyi Geceler",1)
        print("İyi Geceler")


speak("Hoş geldin")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        
        elif "ara" in statement:
            statement = statement.replace("ara","")
            search_web(statement)
            

        elif "kendini kapat" in statement or "kapan" in statement or "çalışmayı durdur" in statement:
            speak('kapatılıyor. Hoşça kal')
            print('kapatılıyor. Hoşça kal')
            break


        elif 'saat kaç' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Şu anda saat {strTime}",1)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)











