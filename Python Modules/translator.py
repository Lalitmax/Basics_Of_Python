import os
from gtts import gTTS

# This module is imported so that we can
# play the converted audio

from playsound import playsound


# It is a text value that we want to convert to audio
text_val = "tum kaise ho .."


# slow =False means high speed voice set normal
obj = gTTS(text=text_val, lang="en", slow=False)

# Here we are saving the transformed audio in a mp3 file named
# exam.mp3
obj.save("exam2.mp3")

# Play the exam.mp3 file

playsound("exam2.mp3")
# remove file
os.remove("exam2.mp3")
