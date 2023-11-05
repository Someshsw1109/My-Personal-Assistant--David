import speech_recognition as sr #pip install speechrecognition
# import pvporcupine
# import struct


def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language="en-in")
        print(f"You Said : {query}") # 

    except:
        return None


    query = str(query)
    return query.lower()

