from distutils.sysconfig import customize_compiler
import transformer
import pyperclip as pc

text = "u line 1 2 B"
customInput = True

while True:
    if customInput:
        text = input()

    if text in ("break", "exit", "ex"):  # for closing the program
        break

    output = transformer.transformInput(text)
    if not output:
        print("No matches, try again or type \"help\" for help")
    for i in output:
        print(i)
        pc.copy(i)