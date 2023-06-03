# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def power_(a, b):
    if b == 0:
        return 1
    if b > 0:
        return a * power_(a, b - 1)
    if b < 0:
        return (1 / a) * power_(a, b + 1)
    
a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

print(f'A = {a}; B = {b} -> {power_(a, b)}')