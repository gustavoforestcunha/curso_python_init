n = cont = soma = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    soma += n
    cont = cont + 1
print('Você digitou {} numeros e a soma entre eles foi {}.'.format(
    cont - 1, soma - 999))
