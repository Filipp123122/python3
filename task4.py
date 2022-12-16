"""
4. Программа принимает действительное положительное число x
и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции
возведения числа в степень и операции **. pow()

Пример: Для значений x = 5, y = -3 результат: 0.008
"""


def get_val(x, y):
    try:
        if y < 0:
            result = 1
            for i in range(y, 0):
                result = result * x
            result = 1 / result
            return f'Для значений x = {5}, y = {-3} результат: {result}'

        else:
            return "Число y должно быть строго отрицательным"

    except TypeError:
        return "Пожалуйста, вводите только числа"
    except ZeroDivisionError:
        return "На ноль делить нельзя"


print(get_val(5, -3))