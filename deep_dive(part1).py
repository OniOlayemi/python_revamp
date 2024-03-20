import numbers

name = 'oluyole'
age = 15

# I think I will stick with this...

print(f"{name} is very heavey in the street at {age} years old")

print('{:b}'.format(age))

print('{:.2f}'.format(age))

print(f'{age:.4f}')

l1 = [1, 3, 5, 6]
l2 = [2, 5, 7,8]

print(id(l1))
print(id(l2), 'first l2')

l1 = l1 + l2

print(id(l1), "after")

l1 =[1, 3, 5, 6]
l2 =[1, 3, 5, 6]
print(id(l1))
print(id(l2))

#recap on nameedtuple

from collections import namedtuple

pint = namedtuple("point", 'x, y, z')

p1 = pint(2, 'abc', [3, 5,6])

print(p1)


x, y, z = p1
print(x,'take it', y, z)


class point:
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = (x, y)
        else