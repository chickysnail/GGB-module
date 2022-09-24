
import sys
sys.path.append('../GGB_module')
from functions import *


usages = {
    point: 
        "(name) point|pnt (x y) \n Note: if x y not specified, then x y are random in range [-5,5]",
    pointOn:
        "(name) pointon|on [object name to put the point on]",
    line:
        "(name) line|ln [(x y)|(point)] [(x y)|(point)]",
    segment:
        "(name) segment|segm [(x y)|(point)] [(x y)|(point)]",
    ray:
        "(name) ray [(x y)|(starting point)] [(x y)|(second point)]",
    midpoint:
        "(name) midpoint|mid [point] [point]",
    bisectionline:
        "(name) bisector|serper|srpr [point] [point]",
    parallel:
        "(name) parallel|parl [pivot point] [point on given line] [point on given line] \n"\
        "OR \n"\
        "(name) parallel|parl [pivot point] [line]",
    perpline:
        "(name) perpendicularline|perl [pivot point] [point on given line] [point on given line] \n"\
        "OR \n"\
        "(name) perpendicularline|perl [pivot point] [line]",
    perpsegment:
        "(name) perpendicularsegment|perpsegm|pers [pivot point] [point on given line] [point on given line] \n"\
        "OR \n"\
        "(name) perpendicularsegment|perpsegm|pers [pivot point] [line]",
    anglebisector:
        "(name) anglebisector|bisec|rat [point] [pivot point] [point] \n"\
        "OR \n"\
        "(name) anglebisector|bisec|rat [line] [line]",
    intersect:
        "(name) intersect|inter|int [line_1 point] [line_1 point] [line_2 point] [line_2 point] \n"\
        "OR \n"\
        "(name) anglebisector|bisec|rat [line_1] [line_1]",
    hide:
        "(object to hide) hide",
    show:
        "(object to show) show",
}

beforeUsage = f"""
Usage:
 - obligatory arguments are in [these brackets]
 - optional arguments are in (these brackets)
 - sign "|" is logical or
"""

# case 1: help outputs all functions with their description
# case 2: help [functionCallName] epxlains a function adn its psosible uasges 

def askGeneralHelp(): # case 1
    with open("texts/help.txt", mode='r', encoding="utf-8") as reply:
        return reply.read()

def askSpecificHelp(func): # case 2
    text = beforeUsage + usages[func]
    return text


if __name__=="__main__":
    print(askSpecificHelp(intersect))