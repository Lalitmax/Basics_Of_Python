import time
import pyscreenshot
import random
t=random.randint(1,1000)
g=str(t)+".png"
time.sleep(2)
image = pyscreenshot.grab()
# image.show()

image.save(r"C:\Users\lalit\OneDrive\Videos\h"+g)