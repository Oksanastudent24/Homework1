import math

def square(a):
    return math.ceil(a * a)

a = float(input('Введите сторону квадрата: '))
print(f"Площадь квадрата: {square(a)}")