from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de seu nascimeto com 4 digitos:'))
idade = atual - nasc
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE.')
elif idade < 18:
    print(f'Você tem {idade} anos e faltam {18 - idade} ano(s), para seu alistamento, portanto seu alistamento será em {nasc + 18}.')
else:
    print(f'Você tem {idade} anos e deveria ter se alistado há {idade - 18} ano(s), portanto o ano do seu alistamento foi em {nasc + 18}.')
