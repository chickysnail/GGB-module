import re
import conf

def capitalize(s:str, do=conf.CAPITALIZE):
    if do:
        return s.capitalize()
    return s


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
    # values: (name) (line) (x y) (pointName) (x y) (pointName) 
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
            arg[i] = capitalize(pntName[i]) 

    definition = ""
    if sName is not None:
        definition += f"{sName}="
    definition += f'Line({arg[0]}, {arg[1]})'
    return definition

def segment(values):
    # values: (name) (segment) (x y) (pointName) (x y) (pointName) 
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
            arg[i] = capitalize(pntName[i])

    definition = ""
    if sName is not None:
        definition += f"{sName}="
    definition += f'Segment({arg[0]}, {arg[1]})'
    return definition

def ray(values):
    # values: (name) (ray) (x y) (pointName) (x y) (pointName) 
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
            arg[i] = capitalize(pntName[i])

    definition = ""
    if sName is not None:
        definition += f"{sName}="
    definition += f'Ray({arg[0]}, {arg[1]})'
    return definition

def midpoint(values):
    # values: (Name) (midpoint) (oName1) (oName2)
    sName = values[0]
    oName1, oName2 = values[2], values[3]
    if oName2 is not None: # capitilize if given points, not segment
        oName1 = capitalize(oName1)
        oName2 = capitalize(oName2)
    
    definition=""
    if sName is not None:
        definition = f'{sName.capitalize()}='
    definition += f'Midpoint({oName1}'
    if oName2 is not None:
        definition += f', {oName2}'
    definition += ')'
    return definition

def bisectionline(values):
    # values: (Name) (bisection) (oName1) (oName2)
    sName = values[0]
    oName1, oName2 = values[2], values[3]
    if oName2 is not None: # capitilize if given points, not segment
        oName1 = capitalize(oName1)
        oName2 = capitalize(oName2)
    
    definition=""
    if sName is not None:
        definition = f'{sName.capitalize()}='
    definition += f'PerpendicularBisector({oName1}'
    if oName2 is not None:
        definition += f', {oName2}'
    definition += ')'
    return definition

def parallel(values):
    # values: (name) (parallel) (point) (line|point) (point)
    sName = values[0]
    arg1, arg2, arg3 = values[2:5]

    definition='' 
    # case 1: Line(Point, Segment(Point, Point))
    # case 2: Line(Point, line)
    if sName is not None:
        definition+=f'{sName}='
    definition+=f'Line({capitalize(arg1)}, '
    if arg3 is not None: # case of 3 points
        definition+=f'Segment({capitalize(arg2)}, {capitalize(arg3)})'
    else: # case of point and line
        definition+=f'{arg2}'
    definition+=')'

    return definition

def perpline(values):
    # values: (name) (perpline) (point) (point|line) (point)
    sName = values[0]
    arg1, arg2, arg3 = values[2:5]

    definition='' 
    # case 1: PerpendicularLine(Point, Segment(Point, Point))
    # case 2: PerpendicularLine(Point, line)
    if sName is not None:
        definition+=f'{sName}='
    definition+=f'PerpendicularLine({capitalize(arg1)}, '
    if arg3 is not None: # case of 3 points
        definition+=f'Segment({capitalize(arg2)}, {capitalize(arg3)})'
    else: # case of point and line
        definition+=f'{arg2}'
    definition+=')'

    return definition

# def perpsegment(values):

def anglebisector(values):
    # values: (name) (perpline) (point|line) (point|line|line) (point)
    sName = values[0]
    arg1, arg2, arg3 = values[2:5]

    definition='' 
    if sName is not None:
        definition+=f'{sName}='
    # case 1: AngleBisector(Point, Point, Point)
    # case 2: AngleBisector(line, line)
    if arg3 is not None: # case 1
        definition+=f'AngleBisector({capitalize(arg1)},{capitalize(arg2)},{capitalize(arg3)})'
    else: # case 2
        definition+=f'AngleBisector({arg1},{arg2})'
    
    return definition



# DONE: point, line, point on, segment, ray, midpoint, parallel line, perpendicular line
# TODO: perpsegment, bisection (serper), bisector, tangent, circumference, hide object, show object, intersection

funNames = {
    point: r"(?:point|pnt)",
    pointOn: r"(?:pointon|pon)",
    line: r"(?:line|ln)",
    segment: r"(?:segment|segm)",
    ray: r"(?:ray)",
    midpoint: r"(?:midpoint|mid)",
    bisectionline: r"(?:bisector|serper|srpr)",
    parallel: r"(?:parallel|parl)",
    perpline: r"(?:perpendicularline|perpline|perl)",
    # perpsegment
    anglebisector: r"(?:anglebisector|bisec|rat)",
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
    # (name) (line) (x y) (pointName) (x y) (pointName) 
    line : re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[line]})"\
            f" +(?:(?:({coordinates})|({name})) +(?:({coordinates})|({name})))"
        ),
    # (name) (segment) (x y) (pointName) (x y) (pointName) 
    segment: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[segment]})"\
            f" +(?:(?:({coordinates})|({name})) +(?:({coordinates})|({name})))"
        ),
    # (name) (ray) (x y) (pointName) (x y) (pointName) 
    ray: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[ray]})"\
            f" +(?:(?:({coordinates})|({name})) +(?:({coordinates})|({name})))"
        ),
    # (Name) (midpoint) (object) (object) 
    midpoint: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[midpoint]}) +(?:(?:({name})) *(?:({name}))?)"
        ),
    # (Name) (bisector) (object) (object) 
    bisectionline: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[bisectionline]}) +(?:(?:({name})) *(?:({name}))?)"
        ),
    # (name) (parallel) (point) (line|point) (point)
    parallel: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[parallel]})"\
            f" +(?:(?:({name})) +(?:({name})))(?: *$| +(?:({name})))"
        ),
    # (name) (perpline) (point) (line|point) (point)
    perpline: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[perpline]})"\
            f" +(?:(?:({name})) +(?:({name})))(?: *$| +(?:({name})))"
        ),
    # (name) (perpsegment) (point) (line|point) (point)
    # perpsegment: 
    # (name) (anglebisector) (point|line) (point|line) (point)
    anglebisector: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[anglebisector]})"\
            f" +(?:(?:({name})) +(?:({name})))(?: *$| +(?:({name})))"
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