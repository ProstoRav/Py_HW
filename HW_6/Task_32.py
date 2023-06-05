# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

def indexes_in_range(lst, mn, mx):
    res_lst = []
    for i in range(len(lst)): 
        if mn <= lst[i] <= mx:
            res_lst.append(i)
    return(res_lst)

lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
mn = 6
mx = 10

print(*(indexes_in_range(lst, mn, mx)))

# Для тех, кто хочет забивать все 20 чисел руками, код рабочий ес чо:)

# def indexes_in_range(lst, mn, mx):
#     res_lst = []
#     for i in range(len(lst)): 
#         if mn <= lst[i] <= mx:
#             res_lst.append(i)
#     return(res_lst)

# n = int(input('Введите количество элементов списка: '))
# lst = []
# for i in range(n):
#     num = int(input(f'Введите {i + 1} элемент списка: '))
#     lst.append(num)
# mn = int(input('Задайте минимум диапазона: '))
# mx = int(input('Задайте максимум диапазона: '))

# print(*(indexes_in_range(lst, mn, mx)))