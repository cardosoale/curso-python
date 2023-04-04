soma = cont = 0

while True:
        
    n = int(input('Digite um número para somar ou 999 para SAIR: '))
    if n == 999:
        break
    soma += n
    cont += 1
    
print(f'Vc digitou {cont} números e sua soma é {soma}')