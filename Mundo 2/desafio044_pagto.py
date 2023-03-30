print('=*' * 10, 'LOJAS CARDOSÃO', '=*'* 10)
preco = float(input('Digite o preço do produto: '))
forma = int(input(' Escolha a forma de pagamento:\n1 - à vista\n2 - à vista no cartão\n3 - 2 x no cartão\n4 - 3 ou mais x no cartão:\n'))
if forma == 1:
    desc = preco * 10 / 100
    pagar = preco - desc
    print(f'Você ganhou R{desc:.2f} de desconto e pagará apenas R${pagar:.2f}')
elif forma == 2:
    desc = preco * 5 / 100
    pagar = preco - desc
    print(f'Você ganhou R{desc:.2f} de desconto e pagará apenas R${pagar:.2f}')
elif forma == 3:
    print(f'Essa forma de pagamento não obtem desconto, você pagará {preco:.2f}')
elif forma == 4:
    mora = preco * 20 / 100
    pagar = preco + mora
    print(f'Essa forma de pagamento terá um acrescimo de 20% (R${mora:.2f}) e o valor à pagar é R${pagar:.2f}')
else:
    print('Forma de pagamento não cadastrada, desculpe.')

