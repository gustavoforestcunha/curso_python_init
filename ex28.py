from random import randint

n = randint(0, 5)
escolhido = int(input('tente acertar o numero secreto: '))
if escolhido == n:
    print('Você acertou, o numero secreto é {}'.format(n))
else:
    print('Você errou! o numero secreto é {}'.format(n))
