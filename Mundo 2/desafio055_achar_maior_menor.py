maior = float(input('Digite o seu peso em Kg: '))
menor = maior
for c in range(4):
    peso = float(input('Digite o seu peso em Kg: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso digitado foi {maior:.2f}kg ')
print(f'O menor peso digitado foi {menor:.2f}kg ')
