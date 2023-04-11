exp = str(input('Digite sua expressão: '))
pilha = []
for c in exp:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão não é valida')