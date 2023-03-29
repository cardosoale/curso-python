numero = int(input('Digite um número de 0 a 9999: '))
numero_str = str(numero).zfill(4)
milhar = numero_str[0]
centena = numero_str[1]
dezena = numero_str[2]
unidade = numero_str[3]
print(f'Milhar: {milhar}')
print(f'Centena: {centena}')
print(f'Dezena: {dezena}')
print(f'Unidade: {unidade}')