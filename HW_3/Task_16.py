# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов 
# в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

n = int(input('Введите количество элементов в массиве: '))
lst = []
for i in range(1, n + 1):
    num = int(input(f'Введите {i} элемент массива: '))
    lst.append(num)
x = int(input('Введите число X: '))
count_ = 0
for i in range(len(lst)):
    if lst[i] == x:
        count_ += 1
print(n)
print(*lst)
print(x)
print(f'-> {count_}')