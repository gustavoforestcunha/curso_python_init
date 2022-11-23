from random import randint
'''n1 = n2 = count = soma = 0
while True:
    n1 = randint(1, 2)
    n2 = int(input('Digite um numero [1 ou 2]: '))
    escolha = str(input('[PAR ou IMPAR?] ')).upper().strip()
    soma = n1 + n2
    count += 1
    if soma % 2 == 0:
        soma = 'PAR'
    if soma % 2 == 1:
        soma = 'IMPAR'
    if soma == escolha:
        break
print(f'Você GANHOU com {count} tentativas!')'''
v = 0
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(
        f'Você jogou {jogador} e computador jogou {computador} e a soma foi {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Ganhou')
            v += 1
        else:
            print('Você Perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou')
            v += 1
        else:
            print('Você Perdeu')
            break
    print('Vamos jogar novamente...')
print(f'GAMO OVER! Você venceu {v} vezes.')
