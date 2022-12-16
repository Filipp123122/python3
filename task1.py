"""
1) Реализовать функцию,
принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""
def division(first_obj, second_obj):
    try:
        return first_obj/second_obj
    except ZeroDivisionError:
        return "Нельзя делить на 0"
try:
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    print(division(first_number, second_number))
except ValueError:
    print("Пожалуйста, вводите только числа")
