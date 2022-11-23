tot = mm = menor = count = 0
barato = ' '
print('=' * 30)
print('LOJA SUPER BARATÃO')
print('=' * 30)
while True:
    produto = str(input('Nome do produto: '))
    preço = int(input('Preço: R$ '))
    count += 1
    tot += preço
    if preço > 1000:
        mm += 1
    if count == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total das compras foi de R${tot:.2f}')
print(f'Temos {mm} produtos custando mais de mil reais.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
