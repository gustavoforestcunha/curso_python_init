n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

m = (n1 + n2) / 2
print('A media final é: {:.1f} '.format(m))
if m >= 7.0:
    print('VOCÊ FOI APROVADO!')
else:
    print('VOCÊ FOI REPROVADO!')
