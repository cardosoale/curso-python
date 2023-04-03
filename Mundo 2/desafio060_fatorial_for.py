n = int(input('Digite um numero para calcular seu fatorial: '))
f = 1
print(f'O fatorial de {n}! é ', end='')
for c in range(1, n + 1):
    print(f'{c}', end='')
    print(f' x ' if c != n else ' = ', end='')
    f *= c
print(f)