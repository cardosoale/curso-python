print('*-'*15)
print('{:^30}'.format('BANCO DO XANDÃO'))
print('*-'*15)
valor = int(input('Digite um valor: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de {ced}')
        if total < 50:
            ced = 20
        if total < 20:
            ced = 10
        if total <10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('*-'*15)