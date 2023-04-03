print('A soma dos múltiplos de 3 entre 3 e 500, ímpares, é: ')
soma = 0
cont = 0
for c in range(3, 500, 3):
    if c % 2 != 0:
        cont += 1
        soma += c        
print(f'O total de números impares entre 3 e 500 é {cont} e o total da soma: {soma}')