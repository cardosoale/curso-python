# programa que pede um número inteiro e mostra se ele é PRIMO ou NÃO
# um número é primo quando é divisível apenas por 1 e por ele mesmo
# n = int(input('Digite um número inteiro para verificar se ele é PRIMO:'))
# if n <= 1:
#     print('ZERO e UM não são considerados números PRIMOS')
# else:
#     primo = True
#     if n >= 2:
#         for i in range(2, n):
#             if n % i == 0:
#                 primo = False
#                 break
#     if primo:
#         print('Este número É PRIMO.')
#     else:
#         print('Este número NÃO É PRIMO.')

n = int(input('Digite um número inteiro para verificar se ele é PRIMO:'))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
if tot == 2:
    print(f'\n\033[mEste número foi divisível apenas por 2 vez(es), portanto é PRIMO.')
else:
    print(f'\n\033[mEste número foi divisível {tot} vez(es), portanto NÃO É PRIMO.')
                
