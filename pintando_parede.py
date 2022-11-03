# considere que a cada 2m quadrados de parede precisa de 1L de tinta para pintar
l = float(input('Qual a largura da parede?: '))
a = float(input('Qual a altura da parede?: '))
m = l*a
t = m/2

print('Largura da parede: {}\n Altura da parede: {}'.format(l, a))
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(l, a, m))
print('Para pintar a parede completa, você precisará de {}L de tinta.'.format(t))
