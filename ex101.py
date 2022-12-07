def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: O voto é opcional.'
    else:
        return f'Com {idade} anos: O voto é obrigatorio.'


nasc = int(input('Qual o ano de nascimento? '))
print(voto(nasc))