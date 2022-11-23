n = count = soma = 0
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    count += 1
    soma += n
print(f'Você digitou {count} numeros e a soma de todos eles foi {soma}')
