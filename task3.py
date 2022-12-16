"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def get_max(*arguments):
    print(sum(sorted(list(arguments), reverse=True)[:2]))


get_max(1, 2, 3)

