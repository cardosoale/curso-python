# programa que lê 6 números inteiros e mostra a soma apenas dos pares
s = 0
cont = 0
for c in range (0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Foi informado {cont} número(s) pares e a soma deles é: {s}')
