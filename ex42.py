r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
'''if r1 == r2 == r3:
    print('Você pode formar um triangulo!')
else:
    print('Você NÃO pode formar um triangulo')'''
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima PODEM formar um triangulo', end=' ')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('os segmentos acima NAO PODEM formar um triangulo')
