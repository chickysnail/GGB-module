import re


# functions: point
# TODO: point on, line

functionNames = {
    "point": r"(point|pnt)",
    "line": r"(line|ln)",
}
name = r"([a-zA-Z]\w*)"
coordinates = r"(\d* \d*)"

class Patterns:
    # point (Name) ([x y])
    point = re.compile(rf"{name}? ?{functionNames['point']} ?{coordinates}?")
    # line (Name) ([[x y]|Point]|[[x y]|Point])
    line = re.compile(rf"{name}? ?{functionNames['line']} ?({coordinates}|{name}&)")

# patterns = {
#     # point (Name) ([x y])
#     "point": re.compile(rf"{name}? ?{functionNames['point']} ?{coordinates}?")
#     # line (Name) ([[x y]|Point]|[[x y]|Point])
#     "line"
# }

for i, row in enumerate(open('inputExample.txt')):
    for match in re.finditer(Patterns.point, row):
        print('Found on line %s: %s' % (i+1, match.groups()))
