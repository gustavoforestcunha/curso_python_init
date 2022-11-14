n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('''===== MENU DE OPÇÕES =====
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA''')
opção = int(input('Digite sua opção: '))
while opção != 5:
    if opção == 1:
        print('A soma dos numeros {} e {} é de {}.'.format(n1, n2, (n1 + n2)))
        opção = int(input('Digite sua opção: '))
    elif opção == 2:
        print('A multiplicação dos numeros {} e {} é de {}.'.format(n1, n2, (n1 * n2)))
        opção = int(input('Digite sua opção: '))
    elif opção == 3:
        if n1 > n2:
            print('O numero {} é maior que {}'.format(n1, n2))
        else:
            print('O numero {} é maior que {}'.format(n2, n1))
            opção = int(input('Digite sua opção: '))
    elif opção == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        opção = int(input('Digite sua opção: '))
else:
    print('Obrigado por utilizar o programa')
