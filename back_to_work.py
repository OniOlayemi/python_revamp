import re

pattern = r'^(string|work)'

text = 'lets come together all string at work'

match = re.findall(pattern, text)

print(match)


pattern = r'[cat]'

text = 'he came with the cat'

match = re.match(pattern, text)

print(match)

pattern = r'[ehcamewiththecat ]'
text = 'he came with the cat'

match = re.match(pattern, text)

if match:
    print("Match found:", match.group())
    print("Start position:", match.start())
    print("End position:", match.end())
    print("Start and end positions:", match.span())
else:
    print("No match found")

y = 4

v = 'fake' if 2 + 2 == y else 'new'
u = [x**2 for x in range(5)]

print(v)
print(u)

def rescale(x, only_translate):
    mean = sum(x) / len(x)
    tranlated = [i - mean for i in range(len(x))]

    if only_translate:
        return tranlated
    else:
        print("i have forgotten the standard deviation formula")
        return tranlated

rescale([3,4,5,6,7,4], True)

def to_list(*args, **kwargs):
    the_list = []
    for x in args:
        the_list.append(x)
    for x in kwargs:
        print(x)
        the_list.append(x)
    return the_list

print(to_list(4,3,2,3,4,5,3,2,1,2,3,34))
print(to_list(b = 1, d = 3, c = 2))
#but I want to get the

#first trial
'''
def to_list(*args, **kwargs):
    the_list = []
    for x in args:
        the_list.append(x)
    x, y for x in enumerate(kwargs):
        print(x)
        the_list.append(x)
    return the_list
'''

#second trial
from collections import namedtuple

def to_list(*args, **kwargs):
    the_list = []
    for x in args:
        the_list.append(x)
    for x in (kwargs.values()):
        print(x)
        the_list.append(x)
    return the_list

print(to_list(4,3,2,3,4,5,3,2,1,2,3,34))
print(to_list(b = 1, d = 3, c = 2))

a = 5

def test(x = 5 * a):
    a = 7
    print(x)
    return x

test(6)
#just checking the local variable stats in R and I was like the same thing happens in python so I gotta check.