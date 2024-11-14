#1.	Сформировать строку из 10 символов.
#На четных позициях должны находится четные цифры, на нечетных позициях - буквы.
import random
import string
#создаем переменную
def generate_string():
    #куда будет записываться результат
    result = []
    
    #четные цифры
    even_digits = ['0', '2', '4', '6', '8']
    #английские буквы, строчные и заглавнык
    letters = string.ascii_letters
#устанавливаем длину пароля 10 символов
    for i in range(10):
        #для четных позиций
        if i % 2 == 0:
            result.append(random.choice(even_digits))
        else:  #для нечетных позиций
            result.append(random.choice(letters))
#возвращаем назад готовый пароль
    return ''.join(result)

#вывод нашей переменной
generated_string = generate_string()
print(generated_string)
