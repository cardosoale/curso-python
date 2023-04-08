# produtos = (
#     ('Produto 1', 10.50),
#     ('Produto 2', 15.99),
#     ('Produto 3', 7.25),
#     ('Produto 4', 12.49)
# )

# print(f'{"PRODUTO":<20}{"PREÇO":>8}')
# for produto in produtos:
#     nome, preco = produto
#     print(f'{nome:<20}{preco:>8.2f}')

lista = ('lápis', 1.75,
         'Borracha', 2,
         'Mochila', 170.99,
         'notebook', 3599.00,
         'régua', 3.99)
print('-' * 40)
print(f'{" LISTAGEM DE PREÇOS ":*^40}')
print('-' * 40)
for index in range(len(lista)):
    if index % 2 ==0:
        print(f'{lista[index]:.<30}', end='')
    else:
        print(f'R${lista[index]:>8.2f}')
print('-' * 40)
