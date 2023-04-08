continuar = 'S'
lista = []
while True:
    if continuar in 'Ss':
        lista.append(int(input('Digite um valor: ')))
        continuar = str(input('Quer continuar? Digite "S" para continuar ou outro qualquer caractere para SAIR: ')).upper().strip()[0]
    else:
        break
print(lista)