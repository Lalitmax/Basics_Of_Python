import pyttsx3

#  for text to speech

engine=pyttsx3.init('sapi5')
engine.say("hello friends how can i help you")
engine.runAndWait()

# changing voice

voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
# test
engine=pyttsx3.init('sapi5')
engine.say("hello friends how can i help you")
engine.runAndWait()

# changing volume
volume=engine.getProperty("volume")
engine.setProperty("volume",2)
# test
engine=pyttsx3.init('sapi5')
engine.say("hello friends how can i help you")
engine.runAndWait()

# changing rate

rate=engine.getProperty("rate")
print(rate)
engine.setProperty("rate",150) # set up new voice
# test
engine=pyttsx3.init('sapi5')
engine.say("hello friends how can i help you")
engine.runAndWait()

#  speaking with number 
engine.say("hello world bro")
engine.say("My current speaking rate is"+str(rate))
engine.runAndWait()
engine.stop()

# saving file to a file

string = ("Lorem Ipsum is simply dummy textof the printing and typesetting industry.")
engine.save_to_file(string,'test.mp3')
engine.runAndWait()




