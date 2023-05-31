larg = float(input('Largura da parede: '))
alt = float(input('altura da parede: '))
ar = larg*alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m2.'.format(larg, alt, ar))
tinta = ar/2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))