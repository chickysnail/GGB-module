import re
# TODO: using pyperclip3 put the result into clipboard (delftstack.com/howto/python/python-copy-to-clipboard)

# e for execute
def point(values):
    oName = values["name"] # oName short for object name
    coords: list = [0,0] if values["coords"] == None else values["coords"].split()
    
    definition=""
    if oName is not None:
        definition = f'{oName}='
    definition += f'({coords[0]}, {coords[1]})'
    
    return definition

def line(values):
    oName = values["name"]
    arg1 = values["arg1"]
    arg2 = values["arg2"]

    def normalise(arg):
        pass

    definition = ""
    if oName is not None:
        definition += f"{oName}="
    #TODO add Line(arg1, arg2)
    definition += f''
    return definition

# functions: point, line
# TODO: point on, line

funNames = {
    point: r"(?:point|p)",
    line: r"(?:line|ln)",
}


# sub patterns
name = r"(?:[a-zA-Z]\w*)"
coordinates = r"(?:\d* \d*)"

class fun:
    # point (Name) ([x y])
    point = re.compile(rf"({name})? ?({funNames[point]}) ?({coordinates})?")
    # line (Name) ([[x y]|Point]|[[x y]|Point])
    line = re.compile(rf"({name})? ?({funNames[line]}) ?(?:({coordinates}|{name}) ({coordinates}|{name}))")


for i, row in enumerate(open('inputExample.txt')):
    print(f"-{i+1}-")

    for match in re.finditer(fun.line, row):
        print('Found on line %s: %s' % (i+1, match.groups()))

    for match in re.finditer(fun.point, row):
        cutcmd = match.groups()
        if re.search(cutcmd[1], funNames[point]):
            ggbcomand = point({"name": cutcmd[0], "coords": cutcmd[2]})
        print(ggbcomand)
        print('Found on line %s: %s' % (i+1, match.groups()))

    print()