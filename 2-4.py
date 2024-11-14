try:
    #ввод списка
    list1 = (input("Введите значения списка: "))
    my_list = list(map(int, list1.split()))

    #подсчет частоты
    frequency = {}

    for item in my_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    #определение наиболее часто встречающегося значения
    most_common_value = max(frequency, key=frequency.get)

    #вывод результата
    print(most_common_value)

except ValueError: #проработка ошибки
    print("Введите корректные значения.")
