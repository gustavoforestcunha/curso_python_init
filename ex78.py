valores = []
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}:')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f' Os valores digitados foram: {valores}')
print(f'o maior valor digitado foi {maior} nas posições', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f' {i}... ', end='')
print(f'o menor valor digitado foi {menor} nas posições', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f' {i}... ', end='')
print(f'os valores organizados ficam {sorted(valores)}')
