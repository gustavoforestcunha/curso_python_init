resp = 'S'
valores = []
while resp in 'Ss':
    valores.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso')
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
print('programa encerrado')
print(f'A lista completa é: {valores}')
valorespar = valores[:]
if valorespar % 2 == 0:
    print(valorespar)
