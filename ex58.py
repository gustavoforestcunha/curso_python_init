from random import randint
count = 1
n = randint(0, 10)
escolhido = int(input('tente acertar o numero secreto: '))
while escolhido != n:
    print('Você errou! tente novamente!')
    escolhido = int(input('tente acertar o numero secreto: '))
    count = count + 1
if escolhido == n:
    print('Você acertou, o numero secreto é {} e você precisou de {} tentativas até acertar o numero'.format(n, count))
