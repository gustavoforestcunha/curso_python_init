lista = []
pares = []
impares = []
for n in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
lista.append(pares[:])
lista.append(impares[:])
print(f'Todos os valores digitados são: {lista}')
print(f'Os valores pares digitados em ordem crescente são: {sorted(pares)}')
print(
    f'Os valores impares digitados em ordem crescente são: {sorted(impares)}')
