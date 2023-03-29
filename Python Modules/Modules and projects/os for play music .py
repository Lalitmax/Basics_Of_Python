import os
import random
n=random.randint(0,7)

music_directory='C:\\Users\\lalit\\Music'

music=os.listdir(music_directory)

os.startfile(os.path.join(music_directory,music[n]))