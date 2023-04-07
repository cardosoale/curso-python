extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
pos = int(input('Digite um número de 0 a 20: '))
print(f'O número que vc digitou foi \033[7m{extenso[pos]}\033[m')