
def are_sets_equal(list1, list2):
    
    #преобразуем списки в множества
    set1 = set(list1)
    set2 = set(list2)
    
    #сравниваем множества
    return set1 == set2

#ввод списков
list1 = input("Введите 1 список элементов через пробел: ")
list2 = input("Введите 2 список элементов через пробел: ")
#вывод результата
print(are_sets_equal(list1, list2))



