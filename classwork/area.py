
import math 

def rectangle(length, width):
    return length*width 


def square(side):
    return side**2

def circle(radius):
    return math.pi*radius**2

#first i did not put arguments inside the function brackets
#initially looked like this def rectangle(): return l*w
#it gives AttributeError: module 'area' has no attribute 'rectangle'