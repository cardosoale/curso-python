numero = int(input('Digite um número de 0 a 9999: '))
# milhar = numero // 1000
# centena = (numero % 1000) // 100
# dezena = (numero % 100) // 10
# unidade = numero % 10
# print(f'Milhar: {milhar}')
# print(f'Centena: {centena}')
# print(f'Dezena: {dezena}')
# print(f'Unidade: {unidade}')
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')



