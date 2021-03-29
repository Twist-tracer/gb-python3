# 5. 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м
# включительно. Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

# диаграмма -> https://drive.google.com/file/d/12XJ15F_8EI58KzivHAFKGJ8rKV9Y4qT9/view?usp=sharing

if __name__ == '__main__':
    result = ''

    for i in range(32, 128):
        result += f'{i}-{chr(i)} '

        if ((i - 31) % 10) == 0:
            result += '\n'

    print(result)
