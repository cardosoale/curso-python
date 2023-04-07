valores = []
par = 0
for c in range(1, 5):
    valor = int(input(f'Digite o numero {c}: '))
    valores.append(valor)
    if valor % 2 ==0:
        par +=1
tupla = tuple(valores)
v9 = tupla.count(9)

print(f'O número 9 aparece {v9} vez(es) na tupla.')
if 3 in tupla:
    print(f'O número 3 aparece pela primeira vez na {tupla.index(3) + 1}ª posição.')
else:
    print('O número 3 não está na tupla.')
print(f'Esta tupla contem {par} números pares.')