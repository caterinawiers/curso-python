a = float(input('Qual é a altura da parede em metros?' ))
l = float(input('E a largura em metros? '))
ar = a*l
print('Logo, a área é de {:.2f} metros quadrados'.format(ar))
print('E você precisa de {:.2f} litros de tinta para pintá-la.'.format(ar/2))