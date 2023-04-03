sex = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sex not in 'MF':
    sex = str(input('Digite novamente seu sexo [M/F]')).strip().upper()[0]
print(f'Sexo {sex} registrado com sucesso')