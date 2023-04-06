from random import randint
v = 0
while True:
    comp = randint(0, 5)
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('''Vamos jogar par ou ímpar?
Qual sua escolha?
PAR OU ÍMPAR [P/I]?
''')).upper().strip()[0]
    if tipo not in 'PI':
        break
    jogador = int(input('Agora digite um número de 0 a 5: '))
    if jogador not in range (0, 6):
        break
    comp = randint(0, 5)
    total = comp + jogador
    print('-='*25)
    print(f'O COMPUTADOR jogou {comp} e VOCÊ jogou {jogador} ', end='')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('\33[32mYOU WIN\033[m')
            print('-='*25)
            v += 1
        else:
            print('\033[31mYOU LOOSE\033[m') 
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('\33[32mYOU WIN\033[m')
            print('-='*25)
            v += 1
        else:
            print('\033[31mYOU LOOSE\033[m') 
            break   
print('-='*25)
print(f'GAME OVER!!! VC teve {v} vitórias consecutivas!!!')

