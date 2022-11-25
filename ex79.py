resp = 'S'
valores = []
while resp in 'Ss':
    valores.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso')
    if valores in valores:
        print('Valor duplicado, digite outro valor: ')
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
print('programa encerrado')
print(f'Você digitou os valores {sorted(valores)}')
