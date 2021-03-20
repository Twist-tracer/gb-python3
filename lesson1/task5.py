# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# диаграмма -> https://drive.google.com/file/d/1humLnGoPjOVVo-ST4AwdSl2Bs7UiBcMC/view?usp=sharing

if __name__ == '__main__':
    num = int(input('Номер буквы в алфавите (1-26): '))

    charNum = ord('a') + num - 1

    print(f'Буква с номером {num} - это {chr(charNum)}')
