preço = float(input('Qual é o preço do produto: R$'))
novo = (preço - (preço*5/100))
print('O produto custava {:.2f}, na promoção de 5% vai custar R${:.2f}'.format(preço, novo))
