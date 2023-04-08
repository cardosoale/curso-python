extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
continuar = 'S'
while True:
    if continuar not in 'SN':
        print('Entrada inválida, tente outra vez: ')
    if continuar in 'N':
        break
    while True:
        pos = int(input('Digite um número de 0 a 20: '))
        if 0 <= pos <=20:
            break  
        print('Tente novamente. ', end='')             
    print(f'O número que vc digitou foi \033[7m{extenso[pos]}\033[m')
    continuar = str(input('Deseja continuar [S/N]:')).upper().strip()[0]
print('FIM')