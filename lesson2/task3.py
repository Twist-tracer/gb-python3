# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.

# диаграмма -> https://drive.google.com/file/d/12XJ15F_8EI58KzivHAFKGJ8rKV9Y4qT9/view?usp=sharing

from math import floor

if __name__ == '__main__':
    n = int(input('Введите число: '))
    result = 0

    while n != 0:
        m = n % 10
        result = result * 10 + m
        n = floor(n / 10)

    print(result)
