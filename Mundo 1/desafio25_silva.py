# nome = input('Digite o nome completo de uma pessoa: ')
# nome = nome.strip()
# if 'SILVA' in nome.upper():
#     print('O nome contém "SILVA".')
# else:
#     print('O nome não contém "SILVA".')

# nome = input('Digite o nome completo de uma pessoa: ')
# nome = nome.strip()
# contem_silva = 'SILVA' in nome.upper()
# print(contem_silva)

nome = input('Digite o nome completo de uma pessoa: ').strip()
print(f"Tem Silva em seu nome? {'silva' in nome.lower()}")
