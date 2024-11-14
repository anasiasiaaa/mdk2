import random
import string
try:
    def generate_password(length, name):

        #символы для пароля (буквы, цифры, знаки)
        characters = string.ascii_letters + string.digits + string.punctuation

        #проверка имени 
        if name:
            password = name + ''.join(random.sample(characters, length - len(name))) 
        else:
            password = ''.join(random.sample(characters, length))

        return password

    #ввод данных от пользователя
    name = input("Введите ваше имя (необязательно): ")
    length = int(input("Введите желаемую длину пароля (не менее 6): "))
    
    #генерация самого пароля с обработкой длины
    if length>6:
        password = generate_password(length, name)
        #вывод при длине больше 6
        print("Сгенерированный пароль:", password)
    else: #вывод при длине меньше 6
        print("Длина пароля слишком маленькая")
except ValueError: #проработка ошибки
    print("Введите корректные значения длины пароля")
