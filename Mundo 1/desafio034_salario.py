salario = float(input('Digite o valor do salario: '))
if salario <= 1250:
    salario = salario + (salario * 15 / 100)
else:
    salario = salario + (salario * 10 /100)
print(salario)