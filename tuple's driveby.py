#checking if tuple and list is homogenous or heterogenous

t = (1,2,3,"b", 6, "r")

l = [1,2,3,"b", 6, "r"]

print(t)
print(l)

#Okay it's heterogenous can I write a loop to check if print function works. cause if I used the True or False, it may
#not work actually

#unpacking a tupple

a,b,c,d,e,f = t

print(a)
print(b)
print(c)


from collections import namedtuple

pt = namedtuple("point", 'x y z')

new = pt(3,4,5)

print(new)
print(f'id is {id(new)}')
print(new.x)
value = list(new)
print(value)

new = pt(new.x, 21, 22)

print(new.z)
print(new.x)
print(new)
print(f'id is {id(new)}')

[*value] = new
value1 = list(new)
print(value1)
print(value)
'''
a = 2,4,5

a = a + (6,7)

print(a)

new = new._replace(x = 5)

print(new)
print(id(new))
new = new._replace(x = 34)
print(id(new))
print(new)
print(dir(namedtuple))
'''

#To really be sure that I am sure of what nemed tuple is

from collections import namedtuple

pt = namedtuple('dd', 'x, y')

new = pt(3,5)

print(new)
print(new.x)

new = new._replace(x = 6)
print(new)

xy = namedtuple('threed', new._fields + ('z', ))
newnew = xy(3,5,1)

print(newnew)

pt.__doc__ = "calculating named tuple"
pt.x.__doc__ = "for x coordinate"
pt.y.__doc__ = "for y coordinate"
print(pt.x.__doc__)
print(pt.y.__doc__)

xy.__new__.__defaults__ = (5, )

newk = xy(3,2)

print(newk)

xy.__new__.__defaults__ = (1,2)

newka = xy(1)
print(newka)

default = xy(0,0,0)

otherside = default._replace(x =3, y = 6)

print(otherside)

#how do I not forget the _replace function and class.__new__.__defaults__