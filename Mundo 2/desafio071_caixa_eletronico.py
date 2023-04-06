notas100 = notas50 = notas20 = notas10 = notas05 = notas02 = 0
while True:
    valor_saque = int(input('Digite um valor para sacar: '))
    while valor_saque % 2 != 0:
        print('Valor invalido, informe apenas múltiplos de R$2')
        valor_saque = int(input('Digite um valor para sacar: '))    
    notas100 = valor_saque // 100
    print(f'Quantidade de notas de R$100: {notas100} notas')    
    notas50 = (valor_saque % 100) // 50
    print(f'Quantidade de notas de R$50: {notas50} notas')
    notas20 = (valor_saque % 50) // 20
    print(f'Quantidade de notas de R$20: {notas20} notas')   
    notas10 = (valor_saque % 20) // 10
    print(f'Quantidade de notas de R$10: {notas10} notas')    
    notas05 = (valor_saque % 10) // 5
    print(f'Quantidade de notas de R$5: {notas05} notas')   
    notas02 = (valor_saque % 5) // 2
    print(f'Quantidade de notas de R$2: {notas02} notas')
    
    