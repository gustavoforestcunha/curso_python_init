from datetime import date

nascimento = int(input(' PREENCHA COM SEU ANO DE NASCIMENTO: '))
ano = date.today().year
idade = ano - nascimento
if idade <= 9:
    print('VOCE TEM {} ANOS E ESTA NA CATEGORIA MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('VOCE TEM {} ANOS E ESTA NA CATEGORIA INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('VOCE TEM {} ANOS E ESTA NA CATEGORIA JUNIOR.'.format(idade))
elif idade > 19 and idade <= 20:
    print('VOCE TEM {} ANOS E ESTA NA CATEGORIA SÊNIOR.'.format(idade))
else:
    print('VOCE TEM {} ANOS E ESTA NA CATEGORIA MASTER.'.format(idade))
