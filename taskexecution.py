#Function used in this python file is of two types
#1- Non-Input
# ex:- Time, Date, Speedtest
import datetime
from Speak import Say
from email import encoders, message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import requests
def Time(): 
    time = datetime.datetime.now().strftime("%I:%M %p")
    Say(time)

def Date():
    date = datetime.datetime.now().strftime("%D")
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def WishMe():
    import time
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
        Say(f"Good Morning its {tt} sir")
    
    elif hour>=12 and hour<=18:
        Say(f"Good Afternoon its {tt} sir")

    else:
        Say(f"Good evening its {tt} sir")

    Say("Hey sir I am your personal assistant how may i help you.... please tell me..... i am always there for you sir....")

def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

#2 - Input
# ex:- google search, wikipedia

def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about", "").replace("what is", "").replace("wikipedia", "")
        import wikipedia
        result = wikipedia.summary(name)
        Say(result)

    elif "google" in tag:
        query = str(query).replace("google", "")
        query = query.replace("search", "")
        import pywhatkit
        pywhatkit.search(query)

    elif "YouTube" in tag:
        query = str(query).replace("YouTube", "")
        import webbrowser
        webbrowser.open("youtube.com")

    # elif "facebook" in tag:
    #     query = str(query).replace("facebook", "")
    #     import webbrowser
    #     webbrowser.open("facebook.com")

    elif "instagram" in tag:
        query = str(query).replace("instagram", "")
        import webbrowser
        webbrowser.open("instagram.com")

    elif "twitter" in tag:
        query = str(query).replace("twitter", "")
        import webbrowser
        webbrowser.open("twitter.com")

    elif "chat GPT" in tag:
        query = str(query).replace("chat GPT", "")
        import webbrowser
        webbrowser.open("chat.openai.com")

    elif "browser" in tag:
        query = str(query).replace("browser", "")
        import os
        Bpath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(Bpath)

    elif "notepad" in tag:
        query = str(query).replace("notepad", "")
        import os
        Npath = "C:\\Windows\\notepad.exe"
        os.startfile(Npath)
        

    elif "IP address" in tag:
        from requests import get
        ip = get('https://api.ipify.org').text
        query = str(query).replace("IP address", "")
        Say("wait a second sir i'm fetching your current IP address just give me some time...")
        Say(f"sir your IP address is {ip}")

    elif "open camera" in tag:
        Say("ok sir please wait...")
        import cv2
        cap = cv2.VideoCapture(0)
        query = str(query).replace("open camera", "")
        while True:
            ret, img = cap.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(50)
            if k==27:
                break;
            cap.release()
            cv2.destroyAllWindows() 

    # elif "State drive" in tag:
    #     query = str(query).replace("SSD", "")
    #     import os
    #     Spath = "C:\\Program Files (x86)\\Samsung\\Samsung Magician\\SamsungMagician.exe"
    #     os.startfile(Spath)

    elif "command prompt" in tag:
        query = str(query).replace("command prompt", "")
        import os
        os.system("start cmd")

    elif "Temperature" in tag:
        query = str(query).replace("Temperature", "")
        import requests
        from bs4 import BeautifulSoup
        search = "Temperature of the current location"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        Say(f"sir the {search} is {temp}")

    elif "Shut Down" in tag:
        query = str(query).replace("Shut Down", "")
        import os
        Say("ok sir your pc will be shutting down within some seconds")
        os.system("shutdown /s /t 5")

    elif "Where is" in tag:
        query = str(query).replace("where is", "")
        from Gmap import GMAP
        Say("ok sir please wait i'm fetching the result.....")
        GMAP()

    elif "spotify" in tag:
        query = str(query).replace("spotify", "")
        import pyautogui
        import os
        import time
        os.system("spotify")
        Say("ok sir please wait i'm opening spotify for you......")
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.write('danza kuduro', interval=0.1)
        for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
            time.sleep(2)
            pyautogui.press(key)

    elif "switch the window" in tag:
        query = str(query).replace("switch the window", "")
        Say("ok sir i am switching the current window to new window as per your order..")
        import pyautogui
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")

    elif "coding profile" in tag:
        query = str(query).replace("coding profile", "")
        Say("ok sir i'm opening your coding profile which is on leetcode platform please wait for some time..")
        import webbrowser
        webbrowser.open("leetcode.com/SomeshRaj09/")

    elif "facebook" in tag:
        query = str(query).replace("facebook", "")
        Say("ok sir please wait i logging in to your facebook account...")

    elif "maximize" in tag:
        query = str(query).replace("maximize", "")
        Say("ok sir i am maximizing the current window")
        import pyautogui
        pyautogui.moveTo(1296, 12)
        pyautogui.leftClick()

    elif "minimise" in tag:
        query = str(query).replace("minimise", "")
        Say("ok sir i am minimizing the current window")
        import pyautogui
        pyautogui.moveTo(1251, 8)
        pyautogui.leftClick()

    elif "close" in tag:
        query = str(query).replace("close", "")
        Say("ok sir i am closing the current window")
        import pyautogui
        pyautogui.moveTo(1339, 0)
        pyautogui.leftClick()
    
    elif "tell me about" in tag:
        query = str(query).replace("tell me about", "")
        Say("Ok sir please wait i'm fetching some info about this")
        import pywhatkit as kit
        resInfo = kit.info(query, lines=2)
        print(resInfo)
        Say(f"Sir, {resInfo}")

    elif "Open My Game website" in tag:
        query = str(query).replace("Open My Game website", "")
        Say("Ok sir please wait, I'm opening your 2048 Game website")
        import webbrowser as wb
        wb.open("https://2048-sr-tech.vercel.app/")
