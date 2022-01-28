from random import sample
from winsound import PlaySound
import pyautogui as psg
import time
from colorama import Fore, Style

#Detect Discord
time.sleep(2)
a = psg.locateOnScreen('./Capture.png')
psg.moveTo(a)
psg.click()

#Detect mic button and unmute
time.sleep(2)
if(psg.locateOnScreen('./unmuted.png')):
    print(f"\n{Fore.RED}You are already unmuted{Style.RESET_ALL}. Continuing the process without unmuting.")
else:
    b = psg.locateOnScreen('./micbutton.png')
    psg.moveTo(b)
    psg.click()
    print(f"\n{Fore.GREEN}U be unmuted now{Style.RESET_ALL}")
    psg.click()

from playsound import playsound
from sounddevice import InputStream
micStream = InputStream(samplerate=16000, blocksize=1024, channels=1,dtype='float32')
micStream.start()
playsound('./apple.mp3')
micStream.stop()

#https://python-sounddevice.readthedocs.io/en/0.4.4/examples.html#play-a-sound-file
# that would work as wel kekw
# ye but rip quality kek
#how about we look up how to play system sound through mic 🤔🤔
#well there needs to be a py lib for that o3o

that didn't work so nvm