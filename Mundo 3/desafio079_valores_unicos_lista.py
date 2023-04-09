lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor add com sucesso!')
    else:
        print('Valor duplicado, não será inserido!')
    r = str(input('Para SAIR digite "N", ou qualquer outro caractere, para continuar: '))
    if r in 'Nn':
        break
print(f'Vc digitou os valores: {lista}')