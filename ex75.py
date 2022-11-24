tupla = int(input('Digite um numero de 0 a 10: ')), int(input(
    "Digite outro valor de 0 a 10: ")), int(input("Digite outro valor de 0 a 10: ")), int(input("Digite outro valor de 0 a 10: ")), int(input("Digite outro valor de 0 a 10: "))
print(tupla)
print(f'O numero 9 apareceu {tupla.count(9)} vezes na tupla.')
if 3 in tupla:
    print(f'O numero 3 apareceu na {tupla.index(3) + 1} posição.')
else:
    print('O valor 3 nao foi digitado nenhuma vez.')
print('Os valores pares foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
