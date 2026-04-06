ip_address = input('Введите IP адрес: ')
parts = ip_address.split('.')

if len(parts) != 4:
    print('НЕТ')
else:
    valid_ip = True
    for part in parts:
        if not part.isdigit():
            valid_ip = False
            break
        num = int(part)
        if num < 0 or num > 255:
            valid_ip = False
            break
    if valid_ip:
        print('ДА')
    else:
        print('НЕТ')