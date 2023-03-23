# cidade = input('Digite o nome de uma cidade: ')
# cidade = cidade.strip()
# if cidade[:5].lower() == 'santo':
#     print('A cidade começa com o nome "Santo".')
# else:
#     print('A cidade não começa com o nome "Santo".')

cidade = str(input('Digite o nome de uma cidade: ')).strip()
# contem_santo = 'santo' in cidade.lower()
# print(contem_santo)
# print(cidade[:5].upper() == 'SANTO')
print('santo' in cidade.lower())