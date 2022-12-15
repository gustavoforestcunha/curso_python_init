from time import sleep
c = ('\033[m',         # 0 sem cor
     '\033[0;30;41m',  # 1 vermelho
     '\033[7;30m',     # 2 branco)


def ajuda(com):
    titulo(f'Acessando o manual do comando \''{com}\'', 4)
    print(c[2], end='')
    help(com)
    print(c[2], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam=len(msg) + 4
    print('-' * tam)
    print(f' {msg}')
    print('-' * tam)
    sleep(1)



comando=''
while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    comando=str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO')
