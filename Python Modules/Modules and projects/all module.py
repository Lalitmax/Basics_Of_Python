import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init('sapi5')

voices = engine.getProperty("voices")
# print(voices[2].id)
engine.setProperty("voices",voices[1])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning ")
        print("Good morning ")
    elif hour >=12 and hour <18:
        speak("good after noon")
    else:
        speak("good evening ")
    
    speak("i am  maxy sir. how may i help you")
    print("i am  maxy sir. how may i help you")

def takecomand():
    # take input microphone
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning...")
        r.pause_threshold = 3
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(query)
        speak(query)
    except Exception as e:
        print(e)
        
        print("say that again please...")
        return "None"
    return query


        
 


    
if __name__ == "__main__":
    while(1):
         wishMe()
         takecomand()
    