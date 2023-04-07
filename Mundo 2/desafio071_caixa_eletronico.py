notas100 = notas50 = notas20 = notas10 = notas05 = notas02 = 0
while True:
    valor_saque = int(input('Digite um valor para sacar ou 0 para encerrar: '))
    if valor_saque == 0:
        break
    while valor_saque % 2 != 0:
        print('Valor invalido, informe apenas múltiplos de R$2')
        valor_saque = int(input('Digite um valor para sacar: '))    
    notas100 = valor_saque // 100
    if notas100 > 0:
        print(f'Quantidade de notas de R$100: {notas100} notas')    
    notas50 = (valor_saque % 100) // 50
    if notas50 > 0:
        print(f'Quantidade de notas de R$50: {notas50} notas')
    notas20 = (valor_saque % 50) // 20
    if notas20 > 0:
        print(f'Quantidade de notas de R$20: {notas20} notas')   
    resto = valor_saque - (notas100 * 100 + notas50 * 50 + notas20 * 20)
    notas10 = resto // 10
    if notas10 > 0:
        print(f'Quantidade de notas de R$10: {notas10} notas')    
    resto -= (notas10 * 10)
    notas05 = resto // 5
    if notas05 > 0:
        print(f'Quantidade de notas de R$5: {notas05} notas')   
    resto -= (notas05 * 5)
    notas02 = resto // 2
    if notas02 > 0:
        print(f'Quantidade de notas de R$2: {notas02} notas')