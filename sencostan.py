# import math
# angulo = float(input('Digite o angulo: '))
# seno = math.sin(math.radians(angulo))
# cosseno = math.cos(math.radians(angulo))
# tangente = math.tan(math.radians(angulo))
# print(f'O angulo de {angulo}, tem o seno de {seno:.2f}º, o cosseno de {cosseno:.2f}º, e a tangente {tangente:.2f}º')

from math import sin, cos, tan, degrees, radians
angulo = float(input('Digite o angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O angulo de {angulo}º tem o seno de {degrees(seno):.2f}º, o cosseno de {degrees(cosseno):.2f}º e a tangente de {degrees(tangente):.2f}º')
