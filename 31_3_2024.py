#writing a code on sets

clue = set(['juice', 'apples', 'chicken', 'vegetables', 'ice', 'drinks'])
on_board = set(['vegetables', 'butter', 'drinks'])

print(on_board.intersection(clue))
print(on_board.issubset(clue))
print(on_board.pop())
#print(on_board.difference_update(clue))
print(on_board)
print(clue.add('butter'))
print(on_board)


def add(**numbers):
    result = 0
    print(numbers)
    for x in numbers:
       result += numbers[x]
    return result

print("----")

print(add(b=5,a=3,v=2,n=4))

import my_calculator

print(my_calculator.add(4,5))
print(my_calculator.multiply(3,2,4))

print(__file__)



from my_testmodule import *

a()
c()
_b()
c()