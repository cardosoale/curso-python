lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor add com sucesso!)
    else:
        print('Valor duplicado, tente outro: ')
    r = str(input('Quer continuar? [S/N]: ')
    if r in 'Nn':
        break
print(lista)