import pandas
import numpy
import sympy


integers = list(range(986000))
'''
test_integers = list(range(5))

print(test_integers)

test_squares = []

for item in test_integers:
    test_squares.append(item ** 2)

print(test_squares)

test_total = 0

del test_squares[0]

print(test_squares)

for item in test_squares:
    if item % 2 == 0:
        pass
    else:
        test_total += item

print(test_total)
'''
squares = []

integers = list(range(986000))


for item in integers:
    squares.append(item ** 2)

total = 0

del squares[0]

for item in squares:
    if item % 2 == 0:
        pass
    else:
        total += item

print(total)



