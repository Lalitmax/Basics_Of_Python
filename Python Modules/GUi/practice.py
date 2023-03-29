from tkinter import*


import datetime
import pyttsx3
import smtplib
import speech_recognition as sr
import webbrowser
import os
import random
import math
import wikipedia
import pywhatkit as wtp

window=Tk()
  





# create date today
date=datetime.datetime.now()
date=str(date)
date=date.split()
date=date[0]

# create random number
r=random.randint(0,7)


# Create a engine
engine=pyttsx3.init()

# set voice of male or female
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# set voice rate
rate=engine.getProperty('rate')
engine.setProperty('rate',178)

# create current datetime
cur_time=datetime.datetime.now().strftime('%H:%M:%S')

# take only hour
hour=int(datetime.datetime.now().hour)
minut=int(datetime.datetime.now().minute)



def speak(text):
    engine.say(text)
    engine.runAndWait()



def wishme():
    if hour>=0 and hour<=12:
        print('good morning sir,\n I am maxi, \n  how may i help you')
        speak('good morning sir, I am maxi, \n  how may i help you')


    elif hour>=12 and hour<=18:
        print('good afternoon sir, \nI am maxi,  how may i help you')
        speak('good afternoon sir, I am maxi,  how may i help you')

    else:
        print('good evening sir,\n I am maxi,  how may i help you')
        speak('good evening sir, I am maxi,  how may i help you')

def sendmail(mail):
    Gmail=None # enter your Gmail
    Psw=None  # enter password
    Port=587 # this is Gmail port number
    To_send=None # which person you want to send mail

    Srvr=smtplib.SMTP('smtp.gmail.com',Port)
    Srvr.starttls()
    Srvr.login(Gmail,Psw)
    Srvr.sendmail(Gmail,To_send,mail)
    print('Email successfully sent')


 
#  take command for do anything   
def command():
    label=Label(window,text='Listening...', font=("Arial",40,"bold"),fg="white",bg="#ba27ab"   )
    label.pack()
    r=sr.Recognizer()
    with sr.Microphone() as mic:
               
        
       
        r.pause_threshold=2
        audio=r.listen(mic)

    try:
        print('recognizing...')
        text=r.recognize_google(audio)
        text=text.lower()
    except Exception as e:
        print(e)
        print("sorry, i don't understand")
        speak("sorry, i don't understand")
        return 'none'
    return text

def doooo(text):
    if text in ['what is the time', "what's the time",'is time','time now',]:
        if hour>=12:
            print(hour,":",minut,'PM')
            speak(str(hour)+":"+str(minut)+'PM')
        else:
            print(hour,":",minut,'AM')
            speak(str(hour)+":"+str(minut)+'Am')

    elif text in ['send mail to lalit','send email to lalit','send mail lalit']:
        print('what do you want to write.. ')
        mail=command()
        sendmail(mail)
    elif text in ["exit","quit"]:
        exit()
    elif text in ["play video","play song","video"]:
        webbrowser.open("www.youtube.com")
        
    elif text in ['open google','google open']:
        webbrowser.open('www.google.com')
        speak('opening google')
        
    elif text in ['open youtube','youtube open']:
        webbrowser.open('www.youtube.com')
        speak('opening youtube')
        
    elif text in ['open telegram','telegram open']:
        webbrowser.open('www.telegram.com')
        speak('opening')
        
    elif text in ['open whatsapp','whatsapp open']:
        webbrowser.open('www.whatsap.com')
        speak('opening whatsapp')
       
    elif text in ['open gmail','gmail open']:
        webbrowser.open('www.gmail.com')
        speak('opening gmail')
    elif text in ['open github','github open']:
        webbrowser.open('www.github.com')
        speak('opening github')
    
    elif text in ['open linkedin','linkedin open']:
        webbrowser.open('www.linkedin.com')
        speak('opening linkedin')
       
    elif text in ['open instagram','instagram open']:
        webbrowser.open('www.instagram.com')
        speak('opening insta gram')
      
    elif text in ['open music','play music','music open','music play']:
        path='C:\\Users\\lalit\\Music'
        music=os.listdir(path)
        os.startfile(os.path.join(path,music[r]))
       
    elif text in ['how are you']:
        
        label=Label(window,text='i am fine.\ntell me how may i help you', font=("Arial",40,"bold"),fg="white",bg="#ba27ab"   )
        label.pack()
        print()
        speak('i am fine, tell me how may i help you')
    elif text in ['what is your name',"what's your name"]:
        print('''well, my name's maxy" \ni wish that everyone\nhad a nickname as cool as mine\nso plz keep small and sort your name  ''')
        speak('''well, my name is maxy, i wish that everyone had a nickname as cool as mine, so plz keep small your name  ''')
    elif text in ['are you marry me',"will you marry me"]:
        print("this is one of things \nwe'd both have to agree\non i'd prefer to keep \nour friendship as it is.")
        speak("this is one of things, we'd both have to agree on i'd prefer to keep  our friendship as it is. ")
    elif text in ['what can you do for me']:
        print("i can do all the work \n which is in my might")
        speak("i can do all the work, which is in my might")
    elif text in ["do something for me"]:
        print("Ask me any problem \ni will try to solve it \nfor you")
        speak("Ask me any problem, i will try to solve it for you")
    elif text in ['date',"what's date","what is date","date","what's the date today","today date","today's date"]:
        print(date)
        speak(date)
    elif text in ["tell me some jokes","tell some jokes","tell me some joke","kucch joke sunao","kuchh jokes sunao",'tell me joke ','tell me jokes']:
        print("Air hostess asked lalu \nPrasad yadav. \nSir are you vegetarian or \nNon vegetarian \nLalu said I am indian \nAir hostess said okay, \nAre you shakahari or mansahari \nLalu said hat sasuri I am Bihari")
        speak("Air hostess asked lalu Prasad yadav. Sir are you vegetarian or Non vegetarian, Lalu said I am indian. Air hostess said okay, Are you shakahari or mansahari, Lalu said hat sasuri I am Bihari")
    elif "wikipedia" in text:
        result=wikipedia.summary(text,sentences=2)
        
        print(result)
        speak(result)
    elif "on youtube" in text:
        try:
            wtp.playonyt(text)
            speak('playing')
        except:
            speak("network Error Occurred ")
        
    elif "how to make" in text:
        try:
            wtp.playonyt(text)
            speak("playing")
        except:
            speak("network Error Occurred ")
        
        
    elif text in ["do you know chitkara university"]:
        print("yes i know chitkara university, \nit is best private university in punjab ")
        speak("yes i know chitkara university, it is best private university in punjab ")
    elif  "factorial" in text:

        fact=str(text)
        fact=fact.split()
        fact=int(fact[-1])
       
        fact=math.factorial(fact)
        print(fact)
        speak(fact)
    elif text in ["open coding ninjas","coding ninjas open","coding ninjas"]:
        webbrowser.open('https://www.codingninjas.com')
        exit()
    elif text in ["open vs code","open visual studio code","vs code open","visual studio code open"]:
        vs_pasth="C:\\Users\\lalit\\OneDrive\\Desktop\\Visual Studio Code.lnk"
        webbrowser.open(vs_pasth)
        










def cbt():
            label=Label(window,text='i am fine.\ntell me how may i help you', font=("Arial",40,"bold"),fg="white",bg="#ba27ab"   )
            

        
            text= command()

            doooo(text)
            label.pack()

    
   
    
    
   #  instantiate an instance of a window

  
window.geometry("1030x1120")
window.title("Maxy")
photo=PhotoImage(file="mic3.png")
window.iconphoto(True,photo)


  


 




window.config(background="#ba27ab")


button=Button(window,image=(photo),
            bg="#ba27ab",
              
              command=cbt,
              activebackground="#ba27ab",
              compound="bottom" )

button.pack()


window.mainloop() # place window on computer screen 





