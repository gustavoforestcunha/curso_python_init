frase = str(input('Digite uma palavra: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('é um palindromo')
else:
    print('NÃO é um palindromo')
