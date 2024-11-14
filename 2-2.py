
try:
    #ввод списка от пользователя
    values =(input("Введите значения через пробел: "))
    my_list = list(map(int, values.split()))

    #ввод значений для замены
    old_value = int(input("Введите старое значение: "))
    new_value = int(input("Введите новое значение: "))

    #замена значений
    my_list = [new_value if x == old_value else x for x in my_list]

    #вывод результата
    print(my_list)
    #проработка исключений
except ValueError:
    print("Проверьте корректность введенных вами значений.")
