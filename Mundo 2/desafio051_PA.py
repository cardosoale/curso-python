# programa que pede o primeiro termo e a razão de uma PA e mostra os 10 primeiros termos
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao

for i in range(primeiro_termo, decimo_termo + razao, razao):
    print(f'{i}', end=' ➝ ')

print('FIM')

# primeiro_termo = int(input('Digite o primeiro termo da PA: '))
# razao = int(input('Digite a razão da PA: '))

# for i in range(10):
#     print(f'{primeiro_termo + i * razao}', end=' ➝ ')
# print('FIM')

