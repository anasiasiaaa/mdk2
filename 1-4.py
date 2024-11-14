#создание переменной
def modify_string(s):
    #проверка что строка начинается на abc
    if s.startswith('abc'):
        return s.replace('abc', 'www', 1)
    else: #работа, если строка начинается не на abc
        return s + 'zzz'
    #ввод строки пользователем
string1 = input("Введите строку: ")
#вывод строки
print(modify_string(string1))
