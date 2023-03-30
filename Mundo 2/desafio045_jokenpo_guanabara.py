from random import randint
from time import sleep
itens = ['PAPEL', 'TESOURA', 'PEDRA']
computador = randint(0,2)
print('''Vamos jogar JOKENPO???
Escolha uma opção:
[0] Papel
[1] Tesoura
[2] Pedra''')
jogador = int(input('Digite uma opção: '))
if jogador not in [0, 1, 2]:
    print('Opção invalida')
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POOO')
print(f'Computador jogou {itens[computador]} e você escolheu {itens[jogador]:}')
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador ==1:
        print('Jogador GANHOU')
    elif jogador == 2:
        print('GANHEI PATÃO KKKK')
    else:
        print('Jogada INVÀLIDA!')
elif computador == 1:
    if jogador == 0:
        print('GANHEI PATÃO KKKK')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador GANHOU')
    else:
        print('Jogada INVÀLIDA!')
elif computador == 2:
    if jogador == 0:
        print('Jogador GANHOU')
    elif jogador == 1:
        print('GANHEI PATÃO KKKK')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVÀLIDA!')

