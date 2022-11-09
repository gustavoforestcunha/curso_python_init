x = int(input('Primeiro termo: '))
y = int(input('Razão:'))
d = x + (10 - 1) * y
for i in range(x, d + y, y):
    print(i)
