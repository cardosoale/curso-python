# num = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))
# print(f'Vc digitou a tupla {num}.')
# print(f'O número 9 apareceu {num.count(9)} vez(es).')
# if 3 in num:
#     print(f'O número 3 apareceu {num.index(3)}ª posição pela primeira vez')
# else:
#     print('O número 3 não aparece nesta tupla.')
# print(f'O numero(s) par(es) nesta tupla: ', end='')
# for c in num:
#     if c % 2 == 0:        
#         print(c, end='')


##VERSÃO IA BING
num = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))
print(type(num))
print(f'Vc digitou a tupla {num}.')
print(f'O número 9 apareceu {num.count(9)} vez(es).')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição pela primeira vez')
else:
    print('O número 3 não aparece nesta tupla.')
pares = []
for c in num:
    if c % 2 == 0:
        pares.append(c)
if len(pares) > 0:
    print(f'O(s) número(s) par(es) nesta tupla foram: {", ".join(map(str, pares))}')
else:
    print('Não há números pares nesta tupla.')