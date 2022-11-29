valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, digite outro valor: ')
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if resp in 'Nn':
        break
print('programa encerrado')
print(f'Você digitou os valores {sorted(valores)}')
