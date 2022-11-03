from datetime import date

nascimento = int(input('DIGITE O ANO DE NASCIMENTO: '))
anoatual = ano = date.today().year
idade = anoatual - nascimento
print('SUA IDADE É DE {} ANOS'.format(idade))
if idade < 18:
    print('VOCE AINDA NAO SE ALISTOU NO SERVICO MILITAR, FALTA(M) {} ANO(S)'.format(
        18 - idade))
elif idade == 18:
    print('VOCE VAI SE ALISTAR ESTE ANO! FIQUE ATENTO!')
else:
    print('VOCE JA PASSOU EM {} ANO(S) O TEMPO DE SE ALISTAR'.format(idade - 18))
