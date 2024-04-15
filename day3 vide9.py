req = [12, 33, 23, 21, 44, 553, 633, 63]

for i in range(len(req)-1, -1, -1):
    print(req[i])

for i in range(len(req)):
    print(req[len(req)-i-1])

print('-' * 5)
for item in reversed(req):
    print(item)

suits = ['Club', 'Hearts', 'Diamond', 'Spade']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'Ace']
deck = []

for i in suits:
    for j in ranks:
        it = j + ' ' + i
        deck.append(it)

print(deck)

v = [j + " " + i for i in suits for j in ranks]
print("v is ", v )
'''
it = [range(2, 11)]
print(it)
'''

it = tuple(range(2,11))
print(it)

it = list(range(2, 11))
print(it)

it = list(range(2, 11)) + list('ajcd')
print(it)
from collections import namedtuple

Cards = namedtuple('Card', "Rank Suits ")


class myowncard:
    def __init__(self):
        self.length = length

    def __iter__(self):
        return self.calculateiter(self.length)

    class calculateiter:
        def __init__(self, length):
            self.length = length

        def __iter__(self):
            print("printing levels")
            return self

        def __next__(self):
            if self.i >= 10:
                raise StopIteration
            else:
                print("printing the next now")
            return self

b = myowncard()

iter(b)
next(b)
