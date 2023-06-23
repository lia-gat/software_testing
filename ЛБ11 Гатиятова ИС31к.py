# Задание 1
n = int(input("Введите кол-во оценок: "))
a = []
for i in range(n):
    m = int(input("Введите оценку: "))
    a.append(m)
print(a)
summ = sum(a)
print(f"Средняя оценка за урок - {summ / n}")
# Задание 2
a = [-1, -2, -3, -4, -5, -6, -7, -8, 0, 1, 2, 3, 4, 5, 6,7]
b = []
for i in a:
    if i < 0:
        b.append(i)
print("Кол-во отрицательных чисел:", len(b))
