# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def ConvertToBinarySystem (number):
    list = []
    while number != 1:
        list.insert(0, number % 2)
        number //=  2
    if number <= 1: list.insert(0, number)
    print(*list)

N = int(input('Введите число N: '))

ConvertToBinarySystem (N)