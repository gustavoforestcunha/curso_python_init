resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
media = soma / quant
print('Você digitou {} numeros e a média foi {:.2f}'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
