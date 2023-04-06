total = maismil = barato = cont = 0
nomebarato = ' '
while True:
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço do produto: R$'))
    cont += 1    
    total += preco
    if preco > 1000:        
        maismil += 1
    if cont == 1 or preco < barato:
        barato = preco
        nomebarato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]?')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi {total:.2f}')
print(f'O total de produtos que custam mais de Mil Reais é {maismil}.')
print(f'O produto mais barato custou R${barato:.2f} e foi {nomebarato}')