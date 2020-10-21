import speech_recognition as sr
import pyttsx3
import datetime
from selenium import webdriver
import os
import time
import subprocess

engine=pyttsx3.init('sapi5')
#voices=engine.getProperty('voices')
#System specific paths. Do not forget change it
tr_voice_id=r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_trTR_Tolga"
en_voice_id=r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',tr_voice_id)
engine.setProperty('rate',150)
#if quiet = 0 it won't speaks
quiet = 0
print('çalıştırılıyor')

def speak(text,override=0):
    if quiet != 0 or override != 0:
        engine.say(text)
        engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone(1) as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='tr')
            print(f"user said:{statement}\n")

        except Exception:
            #if e != "":
                #print(f"Exception name{e}")
            speak("Lütfen tekrar eder misin?")
            return ""
        return statement