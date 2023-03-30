n1 = float(input('Digite a nota 1: '))
n2 = float(input(('Digite a nota 2: ')))
media = (n1 + n2) / 2
print(f'Sua média foi {media:.1f}')
if media < 5:
    print('Você está REPROVADO!')
elif media >= 5 and media <= 6.9:
    print('Você está em RECUPERAÇÃO')
else:
    print('Você foi APROVADO!!')
