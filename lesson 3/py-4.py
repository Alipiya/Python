'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное. Пример:
45 -> 101101
3 -> 11
2 -> 10
'''

a = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное: "))
while n != 0:
    a = str(n%2) + a
    n //=2
print(a)