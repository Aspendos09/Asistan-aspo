from selenium import webdriver
import os
import time
import subprocess
from core import takeCommand
from core import speak
def create_driver():
    driver = webdriver.Firefox(executable_path=os.path.join(os.getcwd(),"browser_driver","geckodriver.exe"))
    driver.set_window_position(-1000, 300)
    driver.set_window_size(800,600)
    driver.implicitly_wait(1)
    return driver
    

def search_web(input):
    input = input.lower()
    #driver for browser
    driver = create_driver()
    if 'youtube' in input.lower(): 
        YouTube(input,driver)
        return
  
    elif 'vikipedi' in input.lower(): 
  
        speak("Opening Wikipedia")
        query = input.lower().replace("vikipedi","")  
        driver.get(f"https://tr.wikipedia.org/w/index.php?search={query}") 
        return
  
    else: 
  
        if 'google' in input: 
  
            query = input.lower().replace("google","")  
            driver.get("http://www.google.com")
            element = driver.find_element_by_name("q")
            element.send_keys(f"{query}")
            element.submit()
            speak("Hangi sayfa ?",1)
            id = takeCommand()
            print(f"alinan girdi ={id}")
            if 'sayfa ' in id:
                id = id.lower().replace("sayfa ","")
                link =driver.find_element_by_xpath(f'/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[{id}]/div/div[1]/a/h3/span')
            link.click()

  
        return


def YouTube(input,driver):
    speak("Opening in youtube") 
    query = input.lower().replace("youtube","") 
    driver.get(f'https://www.youtube.com/results?search_query={query}')
    videolar = driver.find_elements_by_id("video-title")
    speak("Hangi video ?",1)
    id = takeCommand()
    print(f"alinan girdi ={id}")
    if 'video ' in id:
        id = id.lower().replace("video ","")
    videolar[int(id)].click()
    #bug: Listen fonksiyonu yavaş çalışıyor ve çalışmaya başlamadan konuşulursa girdi almıyor