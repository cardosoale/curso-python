homem = mulher_jovem = tot18 = totg = 0
while True:
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            print('Digite um valor válido: ')
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher_jovem += 1
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    totg += 1
    if resp == 'N':
        break

print(f'Foram cadastradas {tot18} pessoas com 18 anos ou mais.')
print(f'Foram cadastrados {homem} homens.')
print(f'Foram cadastradas {mulher_jovem} mulheres com menos de 20 anos.')
print(f'O total de pessoas cadastradas foi {totg}.')