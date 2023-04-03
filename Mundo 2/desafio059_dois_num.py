from time import sleep
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
opcao = 0
while opcao !=5:
    print('''Digite:
        [1] - Somar
        [2] - Multiplicar
        [3] - Maior
        [4] - Novos Números
        [5] - Sair''')
    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma dos dois valores é {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O produto dos dois números é {produto}')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1}, foi o maior valor digitado')
        else:
            print(f'{n2}, foi o maior valor digitado')
    elif opcao == 4:
        print('Digite novos números')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Tente outra vez')
print('END')

    
