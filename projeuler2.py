n_1 = 1

n_2 = 2

total = n_1 + n_2

final = 0

while n_2 < 4000000:
    if n_2 % 2 == 0:
        final += n_2
    else:
        pass

    n_1 = n_2

    n_2 = total

    total = n_1 + n_2

print(final)

