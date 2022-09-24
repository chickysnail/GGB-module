import re
import conf
import help_handler
from functions import *

# DONE: point, line, point on, segment, ray, midpoint, parallel line, perpendicular line,
#  bisection (serper), bisector, hide object, show object, intersection, perpsegment
# TODO: tangent, circle, 


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
    # (name) (parallel) (point) (line|point) $ (point)
    parallel: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[parallel]})"\
            f" +(?:(?:({name})) +(?:({name})))(?: *$| +(?:({name})))"
        ),
    # (name) (perpline) (point) (line|point) $ (point)
    perpline: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[perpline]})"\
            f" +(?:(?:({name})) +(?:({name})))(?: *$| +(?:({name})))"
        ),
    # (name) (perpsegment) (point) (line|point) $ (point)
    perpsegment: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[perpsegment]})"\
            f" +(?:(?:({name})) +(?:({name})))(?: *$| +(?:({name})))"
        ),
    # (name) (anglebisector) (point|line) (point|line) $ (point)
    anglebisector: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[anglebisector]})"\
            f" +(?:(?:({name})) +(?:({name})))(?: *$| +(?:({name})))"
        ),
    # (name) (intersect) (point|line) (point|line) $ (point) $ (point)
    intersect: re.compile(
            f"(?:(?:^ *)|(?:({name})? +))({funNames[intersect]})"\
            f" +(?:(?:({name})) +(?:({name})))(?: *$| +(?:({name})))(?: *$| +(?:({name})))"
        ),
    # (name) (hide)
    hide: re.compile(
            f"({name}) ({funNames[hide]})"
        ),
    # (name) (show)
    show: re.compile(
            f"({name}) ({funNames[show]})"
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