resp = 'S'
valores = []
while resp in 'Ss':
    valores.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso')
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
print('programa encerrado')
print(f'Você digitou os valores {valores}')
print(f'Essa lista tem {len(valores)} valores.')
valores.sort(reverse=True)
print(f'Os valores ao inverso são: {valores}')
if 5 in valores:
    print('o valor 5 faz parte da lista')
else:
    print('o valor 5 não está na lista')
