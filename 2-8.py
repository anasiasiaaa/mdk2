import random

try:
    def create_matrix(n, m):
    #генерация двумерного списка размером n x m
        return [[random.randint(10, 40) for _ in range(m)] for _ in range(n)]

    def find_rows5(matrix):
        rows5 = [] #поиск элементов, делящихся на 5
        for row_index, row in enumerate(matrix):
            if any(element % 5 == 0 for element in row):
                rows5.append(row_index)
        return rows5
    #ввод количества строк и столбцов для матрицы
    N = int(input("Введите количество строк: "))  #количество строк
    M = int(input("Введите количество столбцов: "))  #количество столбцов
    #вывод матрицы
    matrix = create_matrix(N, M)
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)
    #вывод индексов строк, которые делятся на 5
    rows = find_rows5(matrix)
    print("Индексы строк, которые имеют хотя бы один элемент, делящийся на 5: ", rows)
except ValueError:
    print("Введите целочисленные значения количества столбцов и строк.")
