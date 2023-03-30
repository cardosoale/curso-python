num = int(input('Digite um número inteiro: '))
print('''Escolhas as opções:
[1] para converter em BINÁRIO
[2] para converter em OCTAL
[3] para converter em HEXADECIMAL''')
opcao = int(input('Digite um numero para escolher: '))
if opcao == 1:
    print(f'O numero {num} em BINÁRIO é {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} em OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print((f'O número {num} em HEXADECIMAL é {hex(num)[2:]}'))
else:
    print('Opção inválida.')