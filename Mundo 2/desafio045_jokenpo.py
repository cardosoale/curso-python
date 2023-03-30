import random
from time import sleep
lista = ['papel', 'tesoura', 'pedra']
computador = random.choice(lista)
jogador = str(input('Vamos jogar JOKENPO???\n Escolha, papel, tesoura ou pedra: '))
print('...vou ganhar hehe...')
sleep(2)
print(computador)
if computador == jogador:
    print('Empatamos')
elif computador == 'papel' and jogador == 'tesoura':
    print('Você GANHOU')
elif computador == 'papel' and jogador == 'pedra':
    print('GANHEI, PATÃO KKKKK')
elif computador == 'tesoura' and jogador == 'papel':
    print('GANHEI, PATÃO KKKKK')
elif computador == 'tesoura' and jogador == 'pedra':
    print('Você GANHOU')
elif computador == 'pedra' and jogador == 'papel':
    print('Você GANHOU')
elif computador == 'pedra' and jogador == 'tesoura':
    print('GANHEI, PATÃO KKKKK')
else:
    print('Desculpe, não entendi o que vc escolheu')


