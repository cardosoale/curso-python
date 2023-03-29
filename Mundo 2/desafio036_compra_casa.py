casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite seu salario: '))
anos = int(input('Digite em quantos anos pretende pagar: '))
prazo = anos * 12
parcela = casa / prazo
renda = sal * 30 / 100
print(f'> O valor mensal da parcela será R${parcela:.2f}. \n> Em {prazo} meses.\n> O limite mensal para parcela é de R${renda:.2f}')
if parcela <= renda:
    print('Seu financiamento pode ser aprovado!')
else:
    print('O valor da parcela excede, o máximo permitido, e seu empréstimo, será negado!')
print('Obrigado por simular conosco')