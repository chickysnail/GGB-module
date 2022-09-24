import function_handler
import pyperclip as pc
import pasting
from threading import Thread
import help_handler
from functions import *
import re

# Greeting
with open("texts/greeting.txt", mode='r', encoding="utf-8") as greeting:
    print(greeting.read())

# Easy Pasting 
daemon = Thread(target=pasting.background_listener, daemon=True, name='Monitor')
daemon.start()


while True:
    print() 
    text = input()
    splitText = text.split()
    if splitText[0] == "help":
        if len(splitText)==1:
            print(help_handler.askGeneralHelp())
        else:
            for func in funNames.keys():
                if re.search(re.compile('^'+funNames[func]), splitText[1]):
                    print(help_handler.askSpecificHelp(func))
                           
        continue
    

    if text in ("break", "exit", "ex"):  # for closing the program
        break
    
    output = function_handler.transformInput(text)
    if not output:
        print('No matches, try again or type "help" for help')
    for i in output:
        print(i)
        pc.copy(i)