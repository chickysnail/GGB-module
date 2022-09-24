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
    if arg3 is not None: # case 1
        definition+=f'Segment({capitalize(arg2)}, {capitalize(arg3)})'
    else: # case 2
        definition+=f'{arg2}'
    definition+=')'

    return definition

def perpsegment(values):
    # values: (name) (perpsegment) (point) (point|line) (point)
    sName = values[0]
    arg1, arg2, arg3 = values[2:5]

    definition='' 
    # case 1: Segment(Point1,Intersect(Line(Point2,Point3),PerpendicularLine(Point1,Line(Point2,Point3))))
    # adding intersection: Execute({"case 1", "(name)=Intersect(Line(Point2,Point3),PerpendicularLine(Point1,Line(Point2,Point3)))"})
    # case 2: Segment(Point1,Intersect(line,PerpendicularLine(Point1,line)))
    # adding intersection: Execute({"case 2", "(name)=Intersect(line,PerpendicularLine(Point1,line))"})
    if sName is not None: nameInit = f'{sName}='
    else: nameInit = ''
    definition+= 'Execute({"'
    if arg3 is not None: # case 1
        definition+=f'Segment({capitalize(arg1)},'\
            f'Intersect(Line({capitalize(arg2)},{capitalize(arg3)}),PerpendicularLine({capitalize(arg1)},Line({capitalize(arg2)},{capitalize(arg3)}))))",'\
            f'"{nameInit}Intersect(Line({capitalize(arg2)},{capitalize(arg3)}),PerpendicularLine({capitalize(arg1)},Line({capitalize(arg2)},{capitalize(arg3)})))"'
    else: # case 2  
        definition+=f'Segment({capitalize(arg1)},'\
            f'Intersect({arg2},PerpendicularLine({capitalize(arg1)},{arg2})))",'\
            f'"{nameInit}Intersect({arg2},PerpendicularLine({capitalize(arg1)},{arg2}))"'
    definition+='})'

    return definition

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

def intersect(values):
    # values: (name) (intersect) (point|line) (point|line) (point) (point)
    sName = values[0]
    arg1, arg2, arg3, arg4 = values[2:6]

    definition=''
    if sName is not None:
        definition+=f'{capitalize(sName)}='
    definition+='Intersect('
    # case 1: Intersect(Line(Point, Point), Line(Point, Point))
    # case 2: AngleBisector(object, Line(Point, Point))
    # case 3: AngleBisector(object, object)
    if arg3 is not None:
        if arg4 is not None: # case 1
            definition+=f'Line({capitalize(arg1)},{capitalize(arg2)}),Line({capitalize(arg3)},{capitalize(arg4)})'
        else: # case 2
            definition+=f'{arg1},Line({capitalize(arg2)},{capitalize(arg3)})'
    else: # case 3
        definition+=f'{arg1},{arg2}'
    definition+=')'

    return definition

def hide(values):
    # values: (name) (hide)

    sName = values[0] # sName short for self name
    definition=f'SetConditionToShowObject({sName}, false)'
    
    return definition

def show(values):
    # values: (name) (show)

    sName = values[0] # sName short for self name
    definition=f'SetConditionToShowObject({sName}, true)'
    
    return definition


funNames = {
    point: r"(?:point|pnt)",
    pointOn: r"(?:pointon|on)",
    line: r"(?:line|ln)",
    segment: r"(?:segment|segm)",
    ray: r"(?:ray)",
    midpoint: r"(?:midpoint|mid)",
    bisectionline: r"(?:bisector|serper|srpr)",
    parallel: r"(?:parallel|parl)",
    perpline: r"(?:perpendicularline|perpline|perl)",
    perpsegment: r"(?:perpendicularsegment|perpsegm|pers)",
    anglebisector: r"(?:anglebisector|bisec|rat)",
    intersect: r"(?:intersect|inter|int)",
    hide: r"(?:hide)",
    show: r"(?:show)",
}