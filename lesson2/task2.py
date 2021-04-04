# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# диаграмма -> https://drive.google.com/file/d/12XJ15F_8EI58KzivHAFKGJ8rKV9Y4qT9/view?usp=sharing

if __name__ == '__main__':
    n = int(input('Введите число: '))

    even = odd = 0

    while n != 0:
        m = n % 10

        if m % 2 == 0:
            even += 1
        else:
            odd += 1

        n = n // 10

    print(f'в веденном числе {even} четных и {odd} нечетных цифр')
