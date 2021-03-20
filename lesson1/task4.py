# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

# диаграмма ->  https://app.diagrams.net/#G1humLnGoPjOVVo-ST4AwdSl2Bs7UiBcMC

if __name__ == '__main__':
    first = input('Введите 1 букву: ')
    second = input('Введите 2 букву: ')

    firstNum = ord(first) - ord('a') + 1
    secondNum = ord(second) - ord('a') + 1
    distance = abs(firstNum - secondNum) - 1

    print(f'{first} является {firstNum} буквой алфавита')
    print(f'{second} является {secondNum} буквой алфавита')
    print(f'Растояние между ними {distance} букв(ы)')
