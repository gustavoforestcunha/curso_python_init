soma = 0
cont = 0
for i in range(1, 7):
    n = int(input(' Digite um numero: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Voce informou {} numeros pares e a soma foi {}'.format(cont, soma))
