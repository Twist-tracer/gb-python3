# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с
# клавиатуры.

# диаграмма -> https://drive.google.com/file/d/12XJ15F_8EI58KzivHAFKGJ8rKV9Y4qT9/view?usp=sharing

if __name__ == '__main__':
    n = int(input('Введите количество элементов: '))
    row_n = 1

    for i in range(1, n+1):
        print(row_n)
        row_n = (row_n * -1) / 2
