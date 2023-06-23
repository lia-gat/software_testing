# Задание 1
aa = int(input("Введите число(0 прерывает цикл): "))
while aa != 0:
    aa = int(input("Введите число(0 прерывает цикл): "))
    if aa > 0:
        print(aa - aa * 2)
    elif aa < 0:
        print(abs(aa))
# Задание 2
x = int(input("Введите кол-во километров: "))
day = 2
summ = x
while day <= 7:
    x = x + (x * 0.1)
    day += 1
    summ += x
print(summ)
