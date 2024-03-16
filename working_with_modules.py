import math

print(math)

import sys

print(sys)

print(globals())

print(globals()['math'])

print(type(globals()))

print(math.__dict__)

F = math.__dict__['acos']

print(F(0))

lambda: "hello"


import sys
print(sys.modules)
print(sys.meta_path)
print(math.__spec__)
print(math.__package__)

#import functool.partial

def run (a, b=0, c=0):
    print(a,b,c)

#partial(run, 3)
print("__")
#print(dir(sys))
print(sys.__package__)
print(math.__package__)

from functools import partial

print(dir(partial))
#I tried it to check if it is a top-level module but it has no package in it's attribute had to check with dir
print(id(partial))
print(partial.__class__)
#print(partial.__eq__())

