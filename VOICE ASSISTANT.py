import pyttsx3 as p
import speech_recognition as sr
import randfacts
import datetime




#selenium webdriver code
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#WIKIPEDIA...........................................................................
class Infow:
    def __init__(self):
        self.driver = webdriver.Chrome()



    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search=self.driver.find_element(By.XPATH,'//*[@id="searchInput"]') #triggering search bar
        search.click()
        search.send_keys(query)
        search.send_keys(Keys.RETURN) #press enter to search

        #extracting first paragraph and making the assistant speak
        # Wait for the content to load
        try:
            content_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '// *[ @ id = "mw-content-text"] / div[1] / p[1]'))
            )
            content = content_element.text
        except Exception as e:
            content = "Sorry, I couldn't find any relevant information on Wikipedia."

        # Speak the retrieved information
        speak(f"Here is some information about {query}: {content}")

        # Close the WebDriver after use
        self.driver.quit()





#MUSIC...................................................................................
class Music:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)

        try:
            # Wait for the video thumbnails to load before trying to click one
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="dismissible"]'))
            )

            # Find the first video

            video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
            video.click()

            speak("Now playing the video. Enjoy!")

            # Wait for 60 seconds or adjust as necessary
            time.sleep(60)  # Keep the video playing for 60 seconds

        except Exception as e:
            print(e)
            speak("Sorry, I couldn't find a video.")
        # Do not quit WebDriver here; it will remain open after playing the video.
        # Close the WebDriver after use
        self.driver.quit()

#NEWS..........................................................................
import requests
from ss import *
api_address='https://newsapi.org/v2/top-headlines?country=us&apiKey='+key
json_data=requests.get(api_address).json()
ar=[]
def news():
    for i in range(3):
        ar.append("number" + str(i+1) +" " + json_data["articles"][i]["title"]+'.')
    return ar

#FACTS..................................................

#module is imported
url="https://official-joke-api.appspot.com/random_joke"
json_data=requests.get(url).json()

arr=["",""]
arr[0]=json_data["setup"]
arr[1]=json_data["punchline"]
#JOKES............................
def joke():
    return arr
#WEATHER.................................
from ss import *

api_address='http://api.openweathermap.org/data/2.5/weather?q=Kerala&appid='+key2
json_data=requests.get(api_address).json()

def temp():
    temperature=round(json_data['main']['temp']-273,1)
    return temperature

def des():
    description=json_data["weather"][0]["description"]
    return description
#voice assistant code.....................
engine=p.init()  #create an instance of imported modeule's class
rate=engine.getProperty('rate')
engine.setProperty('rate',180)  #to adjust the speed od speaking
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)  #to get female voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

today_date=datetime.datetime.now()

r=sr.Recognizer()
speak("hello. I am your voice assistant")
speak("Today is" + today_date.strftime('%d') + "of"+ today_date.strftime('%B') + "and current time is" +today_date.strftime("%I")+today_date.strftime('%M')+today_date.strftime("%p"))
speak("Temperature in Kerala is" + str(temp()) + "degree celcius"+ "and with "+ str(des()))
speak("what can I do for you?")

with sr.Microphone() as source:
    r.energy_threshold=1000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("I am having a good day")
    speak("what can I do for you")

    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening....")
        audio = r.listen(source)
text2=r.recognize_google(audio)

if "information" in text2:
    speak("you need information related to which topic?")


    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening....")
        audio = r.listen(source)
        infor=r.recognize_google(audio)
    speak('searching {} in wikipedia'.format(infor))
    assist=Infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("you want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening....")
        audio = r.listen(source)
        vid=r.recognize_google(audio)
    print("playing {} on youtube".format(vid))
    assist=Music()
    assist.play(vid)

elif "news" in text2:
    print("sure sir,now i will read news for you")
    speak("sure sir,now i will read news for you")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" or "facts" in text2:
    speak("sure sir")
    x=randfacts.get_fact()
    print(x)
    speak("Did you know that," +x)

elif "joke" or "jokes" in text2:
    speak("sure sir, get ready foe some chuckles")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])









