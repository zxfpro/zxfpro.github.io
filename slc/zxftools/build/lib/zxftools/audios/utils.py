import numpy as np
from IPython.display import display,Audio

def du():
    framerate = 44100 #评率
    t = np.linspace(0,5,framerate*5)
    dataleft = np.sin(2*np.pi*220*t)
    dataright = np.sin(2*np.pi*224*t)
    display(Audio([dataleft, dataright], rate=framerate))
def play_speech(data):
    display(Audio(data,autoplay=True))

