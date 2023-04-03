maior = float(input('Digite o peso da 1ª pessoa em Kg: '))
menor = maior
for c in range(1,5):
    peso = float(input(f'Digite o peso da {c +1}ª pessoa em Kg: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso digitado foi {maior:.2f}kg ')
print(f'O menor peso digitado foi {menor:.2f}kg ')
