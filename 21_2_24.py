l1 = [1,2,3,4]

l2 = [5,6,7,8]
print(id(l1))
l1 = l1 + l2
print(id(l1))
print(l1)

print('\n\n\n')
l1 = [1,2,3,4]
l2 = [5,6,7,8]
print(id(l1))
l1 += l2
print(id(l1))
print(l1)

s1 = 'we need'
s2 = 'oxygen than money'
print(id(s1))
s1 = s1 + s2
print(id(s1))
s1 = 'we need'
s2 = 'oxygen than money'
print(id(s1))
s1 += s2
print(id(s1))


class stuff:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        print("This is my trial and error class")

    def __add__(self, other):
        print('you are trying to add up stuffs using class stuff')
        return f'stuff(name={self.name})'

    def __iadd__(self,other):
        self.name += other.name
        return self.name

c1 = stuff('aabcd')
c2 = stuff('efghh')

c12 = c1 + c2
print(c12)

c1 += c2
print(c1)
c3 = sorted(c1, reverse=True)
print(c3)

sq = [i for i in range(100) if i%2 and i%3 and i%5]
print(sq)


char = list("abdcde")
print(char)
print(char.pop(2))
m = 'justtoconfirmindex'
print(m.index('u'))