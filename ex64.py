count = 0
n = int(input('Digite um numero: '))
while n != 999:
    n = int(input('Digite um numero: '))
    count = count + 1
    soma = n + n
else:
    print('Programa encerrado. Você digitou {} numeros. e a soma de todos eles foi {}'.format(count, soma))
