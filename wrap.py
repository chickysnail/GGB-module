from distutils.sysconfig import customize_compiler
import transformer
import pyperclip as pc


text = "u line 1 2 B"
customInput = True

while text not in ("break", "br", "exit", "ex"):
    if customInput:
        text = input()

    for i in transformer.transformInput(text):
        print(i)
        pc.copy(i)