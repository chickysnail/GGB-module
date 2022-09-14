import transformer
import pyperclip3 as pc

file = "inputExample.txt"
with open(file) as f:
    text = "".join(f.readlines())

text = "u line 1 2 B"
for i in transformer.transformInput(text):
    print(i)
    pc.copy(i)