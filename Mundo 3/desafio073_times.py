bra22 = 'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico Paranaense', 'Atlético Mineiro', 'Fortaleza', 'São Paulo', 'América', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético - GO', 'Avaí', 'Juventude'
print(f' \nA lista dos times participante do Brasileirão 2022 foi:', bra22, '\n')
print(f'Os cinco primeiros colocados no Campenato Brasileiro de 2022 foi: {bra22[0:5]}\n')
print(f'Os quatro últimos colocados foram: {bra22[-4:]}\n')
print(f'Os times participantes em ordem alfabética foram:', sorted(bra22),'\n')
print(f'O time do Juventude terminou em {bra22.index("Juventude") + 1}º colocado.\n')