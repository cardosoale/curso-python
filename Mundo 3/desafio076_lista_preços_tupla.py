produtos = (
    ('Produto 1', 10.50),
    ('Produto 2', 15.99),
    ('Produto 3', 7.25),
    ('Produto 4', 12.49)
)

print(f'{"PRODUTO":<20}{"PREÇO":>8}')
for produto in produtos:
    nome, preco = produto
    print(f'{nome:<20}{preco:>8.2f}')