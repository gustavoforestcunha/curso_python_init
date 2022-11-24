numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')
while True:
    pos = int(input('digite um numero de 0 a 20 [999 para parar.]: '))
    for cont in range(0, len(numero)):
        if pos == cont:
            print(f'O numero escolhido é {numero[cont]}')
    if pos == 999:
        break
print('Programa encerrado.')
