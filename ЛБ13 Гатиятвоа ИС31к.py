# Задание 1
str1 = (map(int, input("Введите номера слов: ").split()))
str2 = list(map(str.lower, input("Введите слова: ").split()))
print(' '.join([str2[i - 1] for i in str1]).capitalize())
# Задание 2
str1 = (map(int, input("Введите номера слов: ").split()))
str2 = list(map(str.lower, input("Введите слова: ").split()))
new_str = ' '.join([str2[i - 1] for i in str1]).capitalize()
print(new_str)
print(*['-'.join(map(str.upper, i)) for i in new_str.split()])
