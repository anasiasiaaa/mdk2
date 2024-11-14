import re

#функция для подсчета цифр в строке
def count_digits(s):
    return len(re.findall(r'\d', s))

#ввод строк от пользователя
a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")
c = input("Введите третью строку: ")
d = input("Введите четвертую строку: ")
e = input("Введите пятую строку: ")

#объединение в массив
array_of_strings = [a, b, c, d, e]

#сортировка массива
sorted_array = sorted(array_of_strings, key=count_digits)

#результат
print(sorted_array)
