import math

#ler angulo
angulo = float(input('digite um angulo em graus:  '))
rad = math.radians(angulo)
#cacular seno, consseno e tangente
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Seno: {}'.format(seno))
print('Cosseno: {}'.format(cosseno))
print('Tangente: {}'.format(tangente))

