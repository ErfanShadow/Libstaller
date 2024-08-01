# Python 3.10
# C0DED BY RIT4X

import os
from colorama import Fore
import art
import time

red = Fore.RED
green = Fore.GREEN
mag = Fore.MAGENTA
yel = Fore.YELLOW
white = Fore.WHITE
sign = yel+"[+]"


def clear():
    os.system("cls")


def ritlib():
    os.system("pip install -r requirements.txt")


clear()
print(red + art.text2art("Libstaller"))
print(sign, green + "Welcome To Our Program")
print(sign, mag + "Choose An Option:\n", red + "1)", green + "Install All Libs\n",
      red + "2)", green + "Show All Libs\n", red + "0)", red + "Exit\n")
answer = input(mag + ">>>" + yel)

if answer == "1":
    clear()
    print(yel + "Wait For Installing. " +
          red + "Don't Close The Tool!" + green)
    print(green + "Wait 10 Seconds Until Tool Restart...")
    time.sleep(10)
    os.system("cls")
    os.system("python Libstaller.py")
    ritlib()
elif answer == "2":
    with open("requirements.txt") as f:
        print(f.read())
        print(green + "Wait 10 Seconds Until Tool Restart...")
    time.sleep(10)
    os.system("cls")
    os.system("python Libstaller.py")
elif answer == "0":
    print(red + "Exiting... Please wait...")
    time.sleep(5)
pass
