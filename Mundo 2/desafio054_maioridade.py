from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(7):
    ano_nasc = int(input(f'Digite o ano de nascimento da {c + 1}ª pessoa com 4 dígitos: '))
    if atual - ano_nasc >= 21:
        maior += 1
    if atual - ano_nasc < 21:
        menor += 1
print(f'A quantidade de maiores de idade é : {maior} pessoas')
print(f'A quantidade de menores de idade é : {menor} pessoas')

