# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть

import random
n = int(input('Введите число монет на столе: '))
count_zero = 0
count_one = 0
print(f'{n} ->', end = ' ')
for i in range(n):
    x = random.randint(0,1)
    print(x, end = ' ')
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
print()
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)