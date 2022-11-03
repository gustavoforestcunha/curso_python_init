km = float(input(' Quantos km o carro rodou?: '))
dias = float(input('Quantos dias o carro ficou alugado?: '))
tkm = km*0.15
tdias = dias*60
total = tdias + tkm
print('O total a pagar do carro é de:R${}'.format(total))
