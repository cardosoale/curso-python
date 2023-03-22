# co = float(input('Digite o comprimento do cateto oposto: '))
# ca = float(input('Digite o comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print(f'A hipotenusa é {hi:.2f}')

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa é {hi:.2f}')