import speech_recognition as sr #pip install speechrecognition

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language="hi-in")
        print(f"You Said : {query}")

    except:
        return ""


    query = str(query)
    return query.lower()
