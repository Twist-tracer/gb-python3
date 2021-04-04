# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака.

# диаграмма -> https://drive.google.com/file/d/1humLnGoPjOVVo-ST4AwdSl2Bs7UiBcMC/view?usp=sharing

if __name__ == '__main__':
    x = 5
    y = 6

    print(f'{x & y}')
    print(f'{x | y}')
    print(f'{x ^ y}')

    print(f'{x >> 2}')
    print(f'{x << 2}')
