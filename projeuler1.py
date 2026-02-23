import pandas
import numpy


numbers = list(range(1000))

del numbers[0]

total = 0

for item in numbers:
    if item % 3 == 0:
        total += item
    elif item % 5 == 0:
        total += item
    else:
        pass

print(total)
