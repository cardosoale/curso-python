s = c = 0
n = int(input('Digite um número para somar, ou 999 para sair: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número para somar, ou 999 para sair: '))
print(f'Vc digitou {c} números e a soma entre eles é {s}')
