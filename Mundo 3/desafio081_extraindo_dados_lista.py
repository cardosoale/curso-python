lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    r = str(input('Quer continuar [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break
print(f'A lista digitada foi {lista}')
print(f'A lista tem {[len(lista)]} elementos')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é: {lista}')
if 5 in lista:
    print('O valor 5 está presente na lista')
else:
    print('O valor 5 não está presente na lista')