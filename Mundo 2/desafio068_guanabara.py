from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR? [P/I] ')).strip().upper()[0]
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER!. Vc venceu {v} vez(es).')