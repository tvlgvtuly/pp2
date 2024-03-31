'''
Создайте генератор, который генерирует квадраты чисел до некоторого числа N.

Напишите программу, использующую генератор для печати четных чисел от 0 до nв форме, разделенной запятыми, где nони вводятся с консоли.

Определите функцию с генератором, который может перебирать числа, делящиеся на 3 и 4, в заданном диапазоне от 0 до n.

Реализуйте генератор, вызываемый squaresдля получения квадрата всех чисел от (a) до (b). Проверьте это с помощью цикла «for» и распечатайте каждое из полученных значений.

Реализуйте генератор, который возвращает все числа от (n) до 0.
'''
#1
def generate_squarenum(n):
    for i in range(n + 1):
        yield i*i
example = list(generate_squarenum(5))
print(*example)

#2
def generate_evens():
    n = int(input('input some number: '))
    for i in range(n + 1):
        if i%2 == 0:
            yield i
example = list(generate_evens())
print(*example, sep = ', ')

#3
def generate_34():
    n = int(input('input some number: '))
    for i in range(n + 1):
        if i%4 == 0 or i%3 == 0:
            yield i
example = list(generate_34())
print(*example, sep = ', ')

#4
def generate_squares(a, b):
    for i in range(a, b+1):
        yield i*i
example = list(generate_squares(1, 5))
print(*example, sep = ', ')

#5
def generate_back(n):
    for i in range(n, -1, -1):
        yield i
example = list(generate_back(5))
print(*example, sep = ', ')