preco = float(input('digite o preço original do produto: '))
novo_preco = preco - preco*5/100
print('O produto custava R${:.2f} e com o desconto de 5% passou a custar R${:.2f}'.format(
    preco, novo_preco))
