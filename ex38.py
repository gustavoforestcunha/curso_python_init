n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
if n1 > n2:
    print('o numero {} é maior que o numero {}.'.format(n1, n2))
elif n1 < n2:
    print('o numero {} é menor que o numero {}.'.format(n1, n2))
else:
    print('os dois valores sao iguais.')
