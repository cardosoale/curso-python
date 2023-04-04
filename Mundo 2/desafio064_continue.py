continuar = 's'
n = int(input('Digite um número: '))
s = c = m = 0
maior = n
menor = maior
while continuar == 's':
    s += n
    c += 1    
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    continuar = str(input('Vc quer continuar[s/n]: ')).lower().strip()[0]
    if continuar == 's':
        n = int(input('Digite um número: '))
m = s / c
print(f'''Vc digitou {c} números e a soma entre eles é {s}. 
A média deles é {m:.0f}.
O maior numero digitado foi {maior}, e o menor foi {menor}''')
    
    
