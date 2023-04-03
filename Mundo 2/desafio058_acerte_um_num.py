from random import randint
computador = randint(0, 10)
palpite = 0
acertou = False
print('''Olá, eu sou o seu computador.
Estou pensando em número!
Será que vc consegue adivinhar?''')
while not acertou:
    jogador = int(input('''Bora, adivinhar?
Dá um chute aí?
'''))
    palpite += 1
    if jogador == computador:
        acertou = True        
    else:
        if jogador > computador:
            print('Quase lá, um pouco menos...')
        else:
            print('Quase lá, um pouco mais...')
print(f'Vc é cara!!! Acertou na {palpite}ª tentativa !!! ')
