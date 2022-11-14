sexo = str(input('Qual o sexo da pessoa? [M/F]')).strip().upper()
while sexo != 'M' and sexo != 'F':
    print('Opção invalida, digite novamente.')
    sexo = str(input('Qual o sexo da pessoa? [M/F]')).strip().upper()
print('O sexo escolhido foi {}'.format(sexo))
