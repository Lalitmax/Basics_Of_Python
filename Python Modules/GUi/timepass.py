from tkinter import *




def pp():
       print("hello")
       label=Label(window,text='Listening', font=("Arial",40,"bold"),fg="white",bg="#ba27ab"   )
            
       label.pack()
        


window=Tk()







 
window.geometry("1030x1120")
window.title("Maxy")


  


 


photo=PhotoImage(file="mic3.png")

window.config(background="#ba27ab")


button=Button(window,image=(photo),
            bg="#ba27ab",
            command=pp,
              
              
              
              activebackground="#ba27ab",
              compound="bottom" )

button.pack()


window.mainloop() # place window on computer screen 
