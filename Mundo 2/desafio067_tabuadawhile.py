while True:
    mult = int(input('Digite um número pra fazer a tabuada, para SAIR, digite um número negativo: '))
    if mult < 0:
        break
    cont = 1  
    tabuada = 0  
    while cont <= 10: 
        tabuada = mult * cont          
        print(f'{mult} x {cont} = {tabuada}')
        cont +=1
        
