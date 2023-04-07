from random import randrange, randint
tupla_aleatoria = tuple(randint(0, 10) for c in range(5))
print(f'Os valores sorteados foram: {tupla_aleatoria}')
print(f'O menor valor soteado foi: {min(tupla_aleatoria)}.')
print(f'O maior valor sorteado foi {max(tupla_aleatoria)}.')