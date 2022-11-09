from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    n = int(input('Digite o ano de nascimento da {}º pessoa: '.format(i)))
    if ano - n >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maior de idade'.format(totmaior))
print('E também tivemos {} pessoas menor de idade'.format(totmenor))
