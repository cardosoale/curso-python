from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de seu nascimento com 4 digitos: '))
idade = atual - nasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')