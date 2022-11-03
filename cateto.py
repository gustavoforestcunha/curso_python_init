'''co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = (co**2+ca**2)**(1/2)
print('a hipotenusa vai medir {}'.format(hi))'''

import math

ca = float(input('comprimento do cateto adjacente: '))
co = float(input('comprimento do cateto oposto: '))
hi = math.hypot(co, ca)
print(hi)
