n = int(input('Digite um número inteiro para verificar se ele é PRIMO:'))
if n <= 1:
    print('ZERO e UM não são considerados números PRIMOS')
else:
    primo = True
    if n >= 2:
        for i in range(2, n):
            if n % i == 0:
                primo = False
                break
    if primo:
        print('Este número É PRIMO.')
    else:
        print('Este número NÃO É PRIMO.')

# n = int(input('Digite um núemro inteiro para verificar se ele é PRIMO:'))
# if n <= 1:
#     print('ZERO e UM não são considerados números PRIMOS')
# else:
#     eh_primo = True
#     for i in range(2, n):
#         if n % i == 0:
#             eh_primo = False
#             break
#     if eh_primo:
#         print('Este número É PRIMO.')
#     else:
#         print('Este número NÃO É PRIMO.')