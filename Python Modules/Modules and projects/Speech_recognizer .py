import speech_recognition as sr



def saysomething():
    # voice recognice (voice pahchanta hai)
    r=sr.Recognizer()
    
    # listen audio from microphone
    with sr.Microphone() as mic:
        # adjuct voice
        # r.adjust_for_ambient_noise(mic)
        r.pause_threshold=1
        # listen voice
        print("Listening...")
        audio=r.listen(mic)

    try:
        print("Recognizing...")
        text=r.recognize_google(audio)
        text=text.lower()
    except Exception as e:
        # print(e)
        print("your voice is not clear")
        return "none"
    return text

if __name__ == "__main__":
    print(saysomething())

