numbers = input('Введите числа, разделяя пробелом: ')
num = list(map(int, numbers.split()))

count = 0
for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] == num[j]:
            count += 1

print(count)