km = float(input('informe a distancia da sua viagem: '))
if km <= 200:
    print('o preço da sua viagem é de {} reais.'.format(km*0.5))
else:
    print('o preço da sua viagem é de {} reais.'.format(km*0.45))
