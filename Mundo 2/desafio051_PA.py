# i = int(input('Digite um número inicial da PA: '))
# n = int(input('Digite um número para a PA: '))
# for c in range (i, i * n, n):
#     print(c, end=' ')

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for i in range(10):
    print(primeiro_termo + i * razao)

