from playsound import playsound  # play sound
import os
from gtts import gTTS  # text to speech hindi
import screen_brightness_control as pct  # for brightness


def speakhindi(english):

    # It is a text value that we want to convert to audio

    # slow =False means high speed voice set normal
    text_val = english
    obj = gTTS(text=text_val, lang="en", slow=False)

    # Here we are saving the transformed audio in a mp3 file named
    # exam.mp3

    # Play the exam.mp3 file
    playsound("exam2.mp3")
    # remove file


speakhindi("tum kaise ho")
