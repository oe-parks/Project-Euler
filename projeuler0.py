integers = list(range(986000))

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



