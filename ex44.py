valorcompra = float(input('Qual o valor da sua compra? '))
print('''Escolha uma forma de pagamento:
[1] A vista (Dinheiro ou PIX) 10% de desconto
[2] A vista no cartão (5% de desconto)
[3] Até duas vezes no cartão (preço normal)
[4] 3x ou mais no cartão (20% de acréscimo)''')
opcao = int(input('Sua opção: '))
if opcao < 1:
    print('Forma de pagamento invalida')
elif opcao > 4:
    print('Forma de pagamento invalida')
elif opcao == 1:
    print('O valor normal da sua compra é de R${}, porém com o desconto de pagamento a vista ficará R${}'.format(
        valorcompra, valorcompra - (valorcompra / 100 * 10)))
elif opcao == 2:
    print('O valor normal da sua compra é de R${}, porém com o desconto de pagamento a vista no cartão, ficará {}'.format(
        valorcompra, valorcompra - (valorcompra / 100 * 5)))
elif opcao == 3:
    print('O valor total da sua compra será de R${} em duas parcelas de R${}'.format(
        valorcompra, valorcompra / 2))
elif opcao == 4:
    parcelas = int(input('Qual a quantidade de parcelas? '))
    print('O total da sua compra ficará R${} em {} parcelas de R${}'.format(
        valorcompra + (valorcompra / 100 * 20), parcelas, (valorcompra + (valorcompra / 100 * 20)) / parcelas))
