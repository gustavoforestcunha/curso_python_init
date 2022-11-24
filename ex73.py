tabela = ('Palmeiras', 'Internacional', 'Fluminense',
          'Corinthians',
          'Flamengo', 'Ahletico PR', 'Atletico MG',
          'Fortaleza',
          'São Paulo',
          'America MG', 'Botafogo', 'Santos', 'Goiás',
          'Bragantino', 'Coritiba', 'Cuiaba',
          'Ceará',
          'Athletico GO', 'Avaí', 'Juventude')
print('Os primeiros 5 colocados da tabela são: ')
print(tabela[:5])
print('Os quatro ultimos colocados da tabela são: ')
print(tabela[-4:])
print('A tabela organizada por ordem alfabetica fica:')
print(sorted(tabela))
print('o time do internacional esta na posição {}'.format(
    tabela.index('Internacional') + 1))
