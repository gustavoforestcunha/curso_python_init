listagem = ('lapis', 1.75,
            'borracha', 2,
            'caderno', 15.90,
            'estojo', 25,
            'transferidor', 4.20,
            'compasso', 9.99,
            'mochila', 120.30,
            'canetas', 22.30,
            'livro', 34.9)
print('-' * 40)
print(f'{"Listagem de preços":^40}')
print('-' * 40)
for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>.2f}')
print('-' * 40)
