import pyttsx3 #pip install pyttsx3


def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[3].id) # You can use male and female voice both firstly you check how many voices are available in your system just uncomment the print(voices) below it will display number of voices available in your system
    #print(voices)
    engine.setProperty('rate',170)
    print("    ")
    print(f"DAVID : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")

# Say(" Hello sir ")


