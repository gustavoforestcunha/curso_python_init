def area():
    l = int(input('Largura (m): '))
    c = int(input('Comprimento (m): '))
    t = l * c
    print(f'A área de um terreno de {l}m x {c}m é {t}m²')


print('Controle de terrenos')
print('-=' * 30)
area()
