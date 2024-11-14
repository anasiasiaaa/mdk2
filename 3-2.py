import hashlib

#создание словаря
vault = {
    "A123": "secret1",
    "B234": "password2",
    "C345": "access3",
    "D456": "codeword4",
    "E567": "keyphrase5"
}

def get_vault_info(password):
    #проверка, есть ли кодовое слово в словаре
    if password in vault.values():
        #поиск номера ячейки
        cell_number = [k for k, v in vault.items() if v == password][0]
        
        #вычисление MD5-хеша кодового слова
        md5_hash = hashlib.md5(password.encode()).hexdigest()
        
        return cell_number, md5_hash
    else:
        return None, None

#запрос кодового слова от пользователя
user_password = input("Введите кодовое слово для доступа к банковской ячейке: ")
cell_number, password_hash = get_vault_info(user_password)
#вывод номера ячейки и хеша
if cell_number:
    print(f"Номер ячейки: {cell_number}")
    print(f"MD5 хеш кодового слова: {password_hash}")
else:
    print("Кодовое слово не найдено.")
