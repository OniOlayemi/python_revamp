import re

subject = 'let us <fight> harder than <our> opponent <that> is <all> right?'

result = re.split("<[^<>]*>", subject)
print(result)

result = re.split("(<[^<>]*>)", subject)
print(result)

result = re.split("(<[^<>]*>)", subject, )
print(result)


text1 = '1234567890'
text2 = '(123) 456-7890'
text3 = '123.456.7890'

pattern = r'^\(?([0-9]{3})\)?[.\- ]?([0-9]{3})[.\- ]?([0-9]{4})$'

match1 = re.sub(pattern, r'(\1) \2-\3', text1)
print(match1)

i = 0
def count():
    global i
    i += 1
    return i

cnt = count()

print(cnt)
print(cnt)

def count():
    i = 0

    def inc():
        nonlocal i
        i += 1

        return i
    return inc
cnt = count()

print(cnt())
print(cnt())
print(cnt())

class returnonly:
    def __init__(self, callee):
        self.callee = callee

    def __iter__(self):
        return self

    def __next__(self):
        return self.callee()

cpp = returnonly(cnt)

for _ in range(5):
    print(cpp.__next__())

def checking():
    i = 0
    i += 2
    return i

cnter = checking()

print(cnter)
print(cnter)

print("_"*23)

pattern = r'^\w+$'

pattern = r'\b[A-Z]{1,10}\b'

pattern = r'\n{5}'

def countd(split=10):
    def reduc():
        nonlocal split
        split -= 1
        return split
    return reduc

aa = countd()

bb = iter(aa, 0)

for _ in bb:
    print(_)

class contit:
    def __init__(self, leave):
        self.contd = leave

    def __next__(self):
        return self.contd()

    def __iter__(self):
        return self
dd = countd(44)
cc = contit(dd)

print('_' * 5)

for _ in range(5):
    print(cc.__next__())
    print(next(cc))

#what can I use the iter on?
#if I am trying to same operation on
#what if I want to iterate between a llst

lst = [1, 2,3,5,6,7,8,4,11,21,32,33,43,54,66,77,56]

class throughit:
    def __init__(self, list, counter=10):
        self.list = list
        self.counter = counter
        self.end = len(list)
        self.index = 0

    def __iter__(self):
        print('iter"s room')
        return self

    def __next__(self):
        print("next's room")
        self.counter -= 1
        print(self.list)
        print(self.index)
        result = self.list[self.index]
        print(result)
        self.index += 1
        return result

ascit = throughit(lst)

iter(ascit)
print(next(ascit))
print(next(ascit))
print(next(ascit))
print(next(ascit))
print(next(ascit))
print(next(ascit))
print(next(ascit))
'''
for u in ascit:
    print(u)
'''

class lsted:
    def __init__(self, list):
        self._list = list

    def __iter__(self):
        return iter(self._list)

asklst = [23,32, 12,21,43,34,54,45]

b2b = lsted(asklst)

for u in b2b:
    print(u)