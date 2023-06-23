# Задание 1
s1 = input("Введите первую строку: ")
s2 = input("Введите первую строку: ")
print(f"Первая строка: {s1}\nВторая строка: {s2}")
if s1[-1] == s2[0]:
    print("ВЕРНО")
else:
    print("НЕВЕРНО")
# Задание 2
word = input("Введите слово: ")
print("Введённое слово:", word)
try:
    print(f"Четвёртая буква в слове {word} - {word[3]}")
except IndexError:
    print("НЕТ")
    