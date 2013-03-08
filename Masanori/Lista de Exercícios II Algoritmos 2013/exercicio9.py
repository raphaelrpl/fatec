import math

area = float(input('Informe tamanho(m²) da area: '))
latas = math.ceil(area / 54)
print('Serão necessarias %i latas.' %latas)
print('Total: R$%i'% (latas * 80))
