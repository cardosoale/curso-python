valor = []
maior = menor = 0
for c in range(5):
    valor.append(int(input(f'Digite um valor para a  posição {c}: ')))
print('-=' * 30)
print(f'Vc digitou os valores: {valor}')
print(f'O maior valor digitado foi {max(valor)}, nas posições: ', end='')
for i, v in enumerate(valor):
    if v == max(valor):
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min(valor)}, nas posições: ', end='')
for i, v in enumerate(valor):
    if v == min(valor):
        print(f'{i}...', end='')
print()
print('-=' * 30)
