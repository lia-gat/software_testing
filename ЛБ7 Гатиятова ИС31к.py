import random
# Задание 1
for i in range(1, 10):
    for j in range(1, 10):
        print("%4d" % (i*j), end='')
    print()
# Задание 2
for i in range(1, 6):
    for j in range(i):
        print(i, end=' ')
    print()
# Задание 3
a = random.sample(range(-10, 10), 10)
for i in a:
    if i < 0:
        continue
    elif i == 0:
        break
    print(f'Корень числа {i} равен {i ** 2}')

