j = ['this', 'is', 'a', 'list']

lst = [i
       for i in j
       if len(i) > 0]

print(lst)

lst2 = [(i, j, k)
        for i in range(5)
        for j in range(6, 11)
        for k in range(11, 16)]

print(lst2)

def lsd():
    x = []
    for i in range(5):
        for j in range(6,11,2):
            for k in range(12, 17,3):

                x.append((i,j,k))
    return x

print(lsd())

#compiled = compile(lsd, filename = 'string', mode= 'eval')
#print(compiled)
size = 3
comb = [[(j, i) for i in range(j+1)] for j in range(size + 1)]
print(comb)

l1 = ['a', 'b', 'c']
l2 = ['1', '2', '3']

lsted = [i + j for i in l1 for j in l2]
print(lsted)

#but if I want it to be in 'square brackets' when each row is done

#first trial
lsted = [[i + j] for i in l1 for j in l2]
print(lsted)

#that's not what I want, I would like the brackets to cover each level
#second trial

lsted = [[i + j for i in l1] for j in l2]
print(lsted)

# I would like to try that without the list comprehension
lst1 = []
lst2 = []
for i in l1:
    for j in l2:
        c = i + j
        lst1.append(c)
    lst2.append(lst1)
print(lst2)
# I attempting to get the result up here in a list comprehension.
lsted = [[(i + j, i+j, i + j) for i in l1] for j in l2]
print(lsted)

# I thought I'd cheat the system
#second trial
# I have issues with where I place my variable definition
lst2 = []
for i in l1:
    lst1 = []
    for j in l2:
        c = i + j
        lst1.append(c)
    lst2.append(lst1)
print(lst2)
