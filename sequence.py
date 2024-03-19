s = 4,2,3,1,6,7

c = hash(s)

print(c)

a = [[0,0]]

print(a)

x = a + a

print(id(x[0]))

print(id(x[1]))

a[0][1] = 123

print(x)

t = ([2, 4], )

t[0][0] = 33

print(t)

t = ()

print(33 in range(100))

d = ((2, 3, 4))

print(d)

#still trying.


s = [[2, 1], [4,2]]
cp = s.copy()

cp[1][0] = 5

print(s)
print(cp)

cp[1] = [5, 3]
print('cp is ', cp)
print('s is ', s)




#what happened is refered to as a shallow copy, it's sequence was copied but the object(index) is still pointing to
#the same memory address.

from copy import deepcopy, copy

d = deepcopy(s)
print(d, '\n\n\n\n\n\n\n\n\n')


list21 = [1,2,3,4,5,6,7]
print(list21[0:4])

list21[0:4] = (11,12,13,14,15)

print(list21)

list21[0] = (1,2,4)
print('...')
print(list21)

for i in range(100):
    try:
        item = list21.__getitem__(i)
    except IndexError:
        break
    print(item * 2)

sl = slice(2, 5, 2)

print(list21[sl])


t  = slice(0, 100, 2).indices(10)

print(t)

