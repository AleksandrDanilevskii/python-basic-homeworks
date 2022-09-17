"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    return [i ** 2 for i in nums]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    """
    функция, которая принимает целое число
    и возвращает True, если число простое.
    Иначе False
    """
    # числа меньше двух точно не являются простыми
    if num <= 1:
        return False
    # учтем двойку
    if num == 2:
        return True
    # сразу можем отфильтровать четные числа -- они не простые
    if not num % 2:
        return False
    # ищем делители для num: если находим -- num не простое
    for i in range(3, num, 2):
        if not num % i:
            return False
    return True



def filter_numbers(nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == 'odd':
        return list(filter(lambda x: x % 2, nums))
    elif filter_type == 'even':
        return list(filter(lambda x: not x % 2, nums))
    elif filter_type == 'prime':
        return list(filter(is_prime, nums))
    else:
        print('Incorrect type value')