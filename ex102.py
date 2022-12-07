def fatorial(n, show=False):
    """_summary_
    Calcula o fatorial de um numero

    Args:
        param n: numero a ser calculado
        param show: (opcional) Mostar ou não a conta


    Returns:
        o valor do fatorial de um numero n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)
