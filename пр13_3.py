file = input('Введите полное имя файла: ')
parts = file.split('\\')
for part in parts:
    print(part)