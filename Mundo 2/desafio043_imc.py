peso = float(input('Digite seu peso em kg: '))
alt = float(input(('Digite sual altura em metros: ')))
imc = peso / alt ** 2
print(f'Seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso')
elif imc < 40:
    print('Você está obeso')
else:
    print('Você tem obesidade mórbida')