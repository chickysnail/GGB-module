import re
# TODO: using pyperclip3 put the result into clipboard (delftstack.com/howto/python/python-copy-to-clipboard)

def point(values):
    # values: (Name) (point) (x y)
    sName = values[0] # sName short for self name
    coords: list = [0,0] if values[2] == None else values[2].split()
    
    definition=""
    if sName is not None:
        definition = f'{sName.capitalize()}='
    definition += f'({coords[0]}, {coords[1]})'
    
    return definition

def pointOn(values):
    # values: (Name) (point on) (object)
    sName = values[0]
    objectName = values[2]

    definition = ""
    if sName is not None:
        definition+=f'{sName.capitalize()}='
    definition+=f'Point({objectName})'

    return definition

def line(values):
    # values: (Name) (line) (x y) (pointName) (x y) (pointName) 
    sName = values[0]
    coord = [None, None]
    pntName = [None, None]
    coord[0], pntName[0] = values[2], values[3]  # One of two values should be None
    coord[1], pntName[1] = values[4], values[5]

    # definition: [name=]Line(arg1, arg2)
    arg=[None, None]
    for i, c in enumerate(coord): # setting arguments from 'values'
        if c is not None: # make from 'x y' '(x, y)
            arg[i] = c.split()
            arg[i] = f'({arg[i][0]}, {arg[i][1]})'
        else: 
            arg[i] = pntName[i]

    definition = ""
    if sName is not None:
        definition += f"{sName}="
    definition += f'Line({arg[0]}, {arg[1]})'
    return definition

def segment(values):
    # values: (Name) (segment) (x y) (pointName) (x y) (pointName) 
    sName = values[0]
    coord = [None, None]
    pntName = [None, None]
    coord[0], pntName[0] = values[2], values[3]  # One of two values should be None
    coord[1], pntName[1] = values[4], values[5]

    # definition: [name=]Segment(arg1, arg2)
    arg=[None, None]
    for i, c in enumerate(coord): # setting arguments from 'values'
        if c is not None: # make from 'x y' '(x, y)
            arg[i] = c.split()
            arg[i] = f'({arg[i][0]}, {arg[i][1]})'
        else: 
            arg[i] = pntName[i]

    definition = ""
    if sName is not None:
        definition += f"{sName}="
    definition += f'Segment({arg[0]}, {arg[1]})'
    return definition

def ray(values):
    # values: (Name) (ray) (x y) (pointName) (x y) (pointName) 
    sName = values[0]
    coord = [None, None]
    pntName = [None, None]
    coord[0], pntName[0] = values[2], values[3]  # One of two values should be None
    coord[1], pntName[1] = values[4], values[5]

    # definition: [name=]Ray(arg1, arg2)
    arg=[None, None]
    for i, c in enumerate(coord): # setting arguments from 'values'
        if c is not None: # make from 'x y' '(x, y)
            arg[i] = c.split()
            arg[i] = f'({arg[i][0]}, {arg[i][1]})'
        else: 
            arg[i] = pntName[i]

    definition = ""
    if sName is not None:
        definition += f"{sName}="
    definition += f'Ray({arg[0]}, {arg[1]})'
    return definition

# DONE: point, line, point on, segment
# TODO: 

funNames = {
    point: r"(?:point|pnt)",
    pointOn: r"(?:pointon|pon)",
    line: r"(?:line|ln)",
    segment: r"(?:segment|segm)",
    ray: r"(?:ray)",
}


# sub patterns
name = r"(?:[a-zA-Z]\w*)"
coordinates = r"(?:-?\d+ -?\d+)"

fun = {
    # (Name) (point) (x y)
    point : re.compile(
            f"(?:(?:({name})? +)|(?:^ *))({funNames[point]})(?: +({coordinates}))? *$"
        ),
    # (Name) (pointon) (object)
    pointOn: re.compile(
            f"(?:(?:({name})? +)|(?:^ *))({funNames[pointOn]})(?: +({name}))? *$"
        ),
    # (Name) (line) (x y) (pointName) (x y) (pointName) 
    line : re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[line]})"\
            f" +(?:(?:({coordinates})|({name})) +(?:({coordinates})|({name})))"
        ),
    # (Name) (segment) (x y) (pointName) (x y) (pointName) 
    segment: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[segment]})"\
            f" +(?:(?:({coordinates})|({name})) +(?:({coordinates})|({name})))"
        ),
    # (Name) (ray) (x y) (pointName) (x y) (pointName) 
    ray: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[ray]})"\
            f" +(?:(?:({coordinates})|({name})) +(?:({coordinates})|({name})))"
        ),
}

def transformInput(inp):
    out = []
    for r, line in enumerate(inp.splitlines()):
        for func in fun.keys(): # looping through all functions' filters

            for match in re.finditer(fun[func], line):
                cutcmd = match.groups()
                if re.search(cutcmd[1], funNames[func], re.MULTILINE): 
                    ggbcommand = func(cutcmd)
                    out.append(ggbcommand)
                    break
    return out

def main():    
    for i, row in enumerate(open('inputExample.txt')):
        print(f"-{i+1}-")

        for match in re.finditer(fun[line], row):
            cutcmd = match.groups()
            if re.search(cutcmd[1], funNames[line]):
                ggbcommand = line(cutcmd)
                print(ggbcommand)

            print('Found on line %s: %s' % (i+1, match.groups()))

        for match in re.finditer(fun[point], row):
            cutcmd = match.groups()
            if re.search(cutcmd[1], funNames[point]):
                ggbcommand = point({"name": cutcmd[0], "coords": cutcmd[2]})
                print(ggbcommand)
            print('Found on line %s: %s' % (i+1, match.groups()))

        print()

if __name__=="__main__":
    main()