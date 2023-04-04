n = int(input('Quantos termos da sequencia de fibonacci, quer mostrar? Ou digite "0" para sair: '))
t1 = 0
t2 = 1
opcao = n
c = 3
if opcao == 1:
    print(f'{t1}', end='')
elif opcao == 2:
    print(f'{t1} => {t2}', end='')
elif opcao == 0:
    print('Saindo...')
else:
    print(f'{t1} => {t2}', end='')

while c <= n:
    t3 = t1 + t2
    print(f' => {t3}', end='')
    c += 1
    t1 = t2
    t2 = t3

print(' => FIM')
