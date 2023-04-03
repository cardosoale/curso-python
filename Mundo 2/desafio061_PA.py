# programa que pede o primeiro termo e a razão de uma PA e mostra os 10 primeiros termos
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
mais = 10
total = 0
while mais != 0:  
    total = total + mais
    while cont <= total:        
        print(f'{primeiro_termo} ➝ ', end='')
        primeiro_termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos à mais vc quer mostrar? '))
print(f'O programa finalizou com {total} progressões')