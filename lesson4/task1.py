# 3.3 В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import cProfile
import random

# def switch_min_max(numbers):
#     # print(numbers)
#     min_number = min(numbers)
#     max_number = max(numbers)
#     min_index = numbers.index(min_number)
#     max_index = numbers.index(max_number)
#     numbers[min_index], numbers[max_index] = max_number, min_number
#     # print(numbers)
#     return numbers


# $ python -m timeit -n 1000 -s "import lesson4.task1 as task1" "task1.switch_min_max(list(range(2, 20)))"
# 1000 loops, best of 5: 8.98 usec per loop

# cProfile.run('switch_min_max(list(range(2, 20)))')
'''
   70 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       17    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 random.py:348(shuffle)
        1    0.000    0.000    0.000    0.000 task1.py:7(switch_min_max)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
       17    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       26    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
'''

# -----------


def switch_min_max(numbers):
    min_number = numbers[0]
    max_number = numbers[0]
    min_index = 0
    max_index = 0
    for index, number in enumerate(numbers):
        if min_number > number:
            min_index, min_number = index, number

        if max_number < number:
            max_index, max_number = index, number

    numbers[min_index], numbers[max_index] = max_number, min_number
    return numbers


# $ python -m timeit -n 1000 -s "import lesson4.task1 as task1" "task1.switch_min_max(list(range(2, 20)))"
# 1000 loops, best of 5: 2.31 usec per loop

# cProfile.run('switch_min_max(list(range(2, 20)))')
'''
   4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task1.py:45(switch_min_max)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
