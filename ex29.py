velocidade = int(input('Digite a velocidade do veiculo: '))
diferenca = velocidade - 80
if velocidade >= 80:
    print('Você foi multado em R${:.2f}'.format(diferenca*7))
else:
    print('Você esta dentro do limite de velocidade.')
