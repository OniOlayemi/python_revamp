
l1 = (2,5,5,6,7)
l2 = (3,1,7,4,2)

c = list(map(lambda a,b: a+ b, l1,l2))

print(c)

#This is definitely the wrong code, I am trying to experiment a program that can multiply itself; if I do not have the
#idea of the number of the items coming into the argument
def multiply(*args):
    a = 1
    for a in args:
        a *= args
    return a

print(multiply(5,7,4,4,5))

# I go again
def multiply(*args):
    a = 1
    for a in args:
        a *= a
    return a

print(multiply(5,7,4,4,5))

# I got the same result so the next thing I will try is to print, I need to know what is happening, is it iterating or
#not. Then maybe I can take a step towatds it.

def multiply(*args):
    b = 1
    for a in args:
        print(a)

multiply(5,7,4,4,5)

#after this move I have an idea or I will try what I should do before I hit the result.

def multiply(*args):
    b = 1
    for a in args:
        a, b = a*b, a
        print(a)

multiply(8,3,4,2,5,6,7,7)

#Okay, I am showing my vulnerability here too, I should just return the function

def multiply(*args):
    b = 1
    for a in args:
        a, b = a*b, a
    return a

print(multiply(8,3,4,2,5,6,7,7))

#There's sstill an error, I should change the value of  a into b


def multiply(*args):
    b = 1
    for a in args:
        b, a = a*b, a
    return a

print(multiply(8,3,4,2,5,6,7,7))

#Hold up I overthought this one, I can just put b in the equation and we will "be" fine... no pun intended. Since the
#value of a is continuously changing

def multiply(*args):
    b = 1
    for a in args:
        b = a*b
    return b

print(multiply(8,3,4,2,5,6,7,7))

#dang! dang!! dang!!!.. it worked.

#So next mission is to write a function that does the same thing using reduce function and decorator, if it is possible
# I think I should start out with the reduced function

from functools import reduce

L1 = [3, 5, 2,7, 4,8,6,11]

print(reduce(lambda a,b: a * b, l1))

# I want to check my result before I make the next move

print(3*5*2*7*8*4*6*11)

#it's not correct? what could have gone wrong sir?
# I will add zero to some of the value, maybe I will figure out what went wrong.

L1 = [3, 5, 2,7, 4,8,6,0]

print(reduce(lambda a,b: a * b, l1))

# I added zero to the last item on the list "index -1" (index -1), and it gave the same answer, so I will just play with
#the zero and try to find out what went wrong, I hope I find it. hold up I can try adding the values after to see what
#could have gone wrong.

L1 = [0, 5, 2, 7, 4, 8, 6, 11]

print(reduce(lambda a,b: a * b, l1))

#Holla, I circle zero through the entire function and it wouldn't change a thing. it's still the same answer
# i guess I need to go read about reduce function again, thank goodness I circled back.

# I ran the code through my ai secretary and it noted that I should have used L1. case sensitive error, let me run that
#again

L1 = [3, 5, 2, 7, 4, 8, 6, 11]

print(reduce(lambda a,b: a * b, L1))

#it gave the right answer, so why did the wrong action give the wrong answer, actually; wrong action should give the
#wrong answer but I need a technical reason
# I found it I wrote a list l1 earlier
#now, let's run it through a decorator


def dec(fn):
    def inner(*args, **kwargs):
        print("we're inside")
        fn(*args, **kwargs)
    return inner

@dec
def mul():
    b = 1
    a,b = a, b*a
    return b

#mul()

#aside from the fact that I do not know where this function will take me, I need to go revise my decorators a little bit
#Now let's move on to other function like zip, I forgotten what zip does

print("c")
"""print(zip(lambda a,b:a+b, l1,l2))"""

#okay a lil trial and error here.

print(zip(l1, l2))

#I will try putting it in a list. let's see

c = list((zip(l1, l2)))

print(c)

#okay, that what zip does
#now, I am moving on to the filter

def something(h, b, c, d, f):
    return h + b + c+ d+ f

#holla, I am on a wrong way, I am thinking about a function I have forgotten, I will research for it later but I think
#filter is used to remove some object and leave some

print(filter(lambda x: x%2 == 0, l2))

c = list(filter(lambda x: x%2 == 0, l2))

print(c)

#so filter removes the odd number and leave the even number. smooth.
#now what is that function I was looking for, the function that reduces the number of element you need to add in
#your function..

#the function is the partial function, I will check it out when it's time.

from functools import partial

def something(h, b, c, d, f):
    return h + b + c+ d+ f

#partial(something(), 6,7,5,4,3)
help(partial)

#So, I cheated. I went to the net to check how to use the partial function

def something(h, b, c, d, f):
    return h + b + c+ d+ f

y = partial(something, 23,24)
print(y(43,22,21))

#try some more stuff, I do not do normally

print("operator\n\n")

import operator

t = operator.add(4,3)
print(t)

t =operator.mul(5,7)
print(t)

#why will I go through that much stress to add up numbers?
print(dir(operator))
import math
print(id(math))

