lista = []
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    r = str(input('Quer continuar [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break
for num in lista:
    if num % 2 == 0:
        par.append(num)
    elif num % 2 == 1:
        impar.append(num)
print(f'A lista digitada foi {lista}')
print(f'A lista somente com números pares é: {par}')
print(f'A lista somente com números impares é: {impar}')

