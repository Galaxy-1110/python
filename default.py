from random import sample
import pyautogui as psg
import time
from colorama import Fore, Style

#Detect Discord
time.sleep(2)
print('a')
a = psg.locateOnScreen('./discord.png')
psg.moveTo(a)
psg.click()

#Detect mic button and unmute
if(psg.locateOnScreen('./unmuted.png')):
    print(f"\n{Fore.RED}You are already unmuted{Style.RESET_ALL}. Continuing the process without unmuting.")
else:
    b = psg.locateOnScreen('./micbutton.png')
    psg.moveTo(b)
    psg.click()
    print(f"\n{Fore.GREEN}U be unmuted now{Style.RESET_ALL}")

#Put the key you have set as hotkey to play the sound in soundboard betewen ' '. (Soundboard must be running)
psg.press('`')
