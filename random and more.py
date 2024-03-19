import  random

l = [10, 20, 30, 40, 50]

rand_index = random.randrange(len(l))

print(l[rand_index])


mor_rand = [random.choice(l) for i in range(len(l))]

print(mor_rand)

print(random.choice(l))

from collections import namedtuple

pick = namedtuple('pick', 'a,b,c,d')
ab = pick(3,4,5,6)

print(ab)

print('___1___')

v = [1, 2, 3,4, 5, 6,7,8,9]

print([random.choice(v) for i in range(5)])

randoms = random.choices(v, k=4)
print(randoms)


suits = 'Ace', 'Spade', 'Club', 'Hearts'

deck = '*2', '*3', '*4', '*5', '*6', '*7', '*8', '*9', '*j', '*q', '*K', '*A'

card = []
for suit in suits:
    for d in deck:
        card.append(suit + d)


print(card)

#minimal deck of cards

m_card = [(suit + d) for suit in suits for d in deck]
print(m_card)


#Trying to write a function that returns a function that returns a function

def func2func (l):
    if l == 1:
        print("monday")
    elif l == 2:
        print("Tuesday")
    elif l == 3:
        print("Wednesday")
    elif l == 4:
        print("Thursday")
    else:
        print("invalid day")

func2func(2)
#named tuple is the like this (3:1, 2:5, g:4)