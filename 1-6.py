def extract_words(sentence, delimiters):
    #заменяем все разделители на пробелы
    for delimiter in delimiters:
        sentence = sentence.replace(delimiter, ' ')
    
    #разделяем строку на слова по пробелам и удаляем пустые строки
    words = [word for word in sentence.split() if word]
    return words
#ввод строки и символов от пользователя
input_string = input("Введите строку с символами: ")
delimiters = input("Введите символы: ")
#выделение слов из текста
words = extract_words(input_string, delimiters)
#вывод результата
print(words)
