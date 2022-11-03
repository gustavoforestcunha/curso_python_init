salario = float(input('Digite seu salario:'))
if salario > 1250:
    print('O seu salário agora é de {} com o aumento de 10%'.format(
        salario+(salario/100*10)))
else:
    print('O seu salário agora é de {} com o aumento de 15%'.format(
        salario+(salario/100*15)))
