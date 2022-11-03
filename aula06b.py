#n = float(input('digite um valor: '))
# print(n)
#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite um valor: '))
#s = n1 + n2
#print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))

from curses.ascii import isspace

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
