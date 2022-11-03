import math

angulo = float(input('digite o angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('o angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('o angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('o angulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))
