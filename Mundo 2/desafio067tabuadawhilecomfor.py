while True:
    mult = int(input('Digite um número pra fazer a tabuada, para SAIR, digite um número negativo: '))
    if mult < 0:
        break
    print('-'*13)
    for c in range(1, 11):
        print(f'{mult} x {c} = {mult*c}')
    print('-'*13)