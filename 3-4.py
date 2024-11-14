#создание списка студентов
students = {
    1: ["Иванов", [4, 5, 3, 4]],
    2: ["Петров", [3, 4, 5, 3]],
    3: ["Сидоров", [5, 5, 4, 4]],
    4: ["Кузнецов", [4, 4, 4, 4]],
    5: ["Семенов", [3, 3, 2, 4]],
    6: ["Федоров", [5, 4, 4, 5]],
    7: ["Дмитриев", [4, 2, 3, 4]],
    8: ["Алексеев", [5, 4, 5, 4]]
}

#функция для вычисления среднего балла студента
def calculate_average(grades):
    return sum(grades) / len(grades)

#форматирование вывода
print("Фамилия студента\tСредний балл")
print("-" * 40)
#вывод значений
for student_number, data in students.items():
    surname = data[0]
    grades = data[1]
    average = calculate_average(grades)
    print(f"{surname}\t\t{average:.2f}")

