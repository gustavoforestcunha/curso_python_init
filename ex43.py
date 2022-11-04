peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você está abaixo do peso ideal, e seu IMC é de {:.2F}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Você está no seu peso ideal, e seu IMC é de {:.2F}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso, e seu IMC é de {:.2F}'.format(imc))
elif imc >= 30 and imc < 40:
    print('Você está OBESO, e seu IMC é de {:.2F}'.format(imc))
else:
    print('Você É UM PLANETA, e seu IMC é de {:.2F}'.format(imc))
