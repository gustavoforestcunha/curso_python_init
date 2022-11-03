casa = float(input('Por favor, inclua o valor do imovel desejado: '))
salario = float(input('Por favor, insira seu salario: '))
tempo = float(
    input('Por favor, insira a quantidade de anos em que você deseja pagar o imovel: '))
prestacao = casa / (tempo * 12)
minimo = salario / 100 * 30
print('A prestação do imovel sera de {:.2f} e o maximo para seu perfil é de {:.2f}.'.format(
    prestacao, minimo))
if prestacao <= minimo:
    print('Você pode comprar o imovel')
else:
    print('Você NÃO pode comprar o imovel')
