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
    print(f"\n{Fore.RED}You are already unmuted{Style.RESET_ALL}\n")
else:
    b = psg.locateOnScreen('./micbutton.png')
    psg.moveTo(b)
    psg.click()
    print(f"\n{Fore.GREEN}U be unmuted now{Style.RESET_ALL}\n")
    time.sleep(10)
    psg.click()
