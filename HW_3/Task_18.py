# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному 
# числу X. Пользователь в первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

n = int(input('Введите количество элементов в массиве: '))
lst = []
for i in range(1, n + 1):
    num = int(input(f'Введите {i} элемент массива: '))
    lst.append(num)
x = int(input('Введите число X: '))
res_i = 0
min_ = abs(x - lst[0])
for i in range(len(lst)):
    count_ = abs(x - lst[i])
    if count_ < min_:
        min_ = count_
        res_i = i
print(n)
print(*lst)
print(x)
print(f'-> {lst[res_i]}')