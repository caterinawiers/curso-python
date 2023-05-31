nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
print('Prazer em te conhecer, {:20}!'.format(nome))
print('Prazer em te conhecer, {:<20}!'.format(nome))
print('Prazer em te conhecer, {:>20}!'.format(nome))
print('Prazer em te conhecer, {:^20}!'.format(nome))
print('Prazer em te conhecer, {:=^20}!'.format(nome))
n1 = int(input('Um valor:' ))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}.'.format(s))
print('A soma vale {}.'.format(n1+n2))
print('A soma vale {}, o produto vale {}, a divisão vale {:.3f}, a divisão inteira é {} e a potência é {}.'.format(s, m, d, di, e))

