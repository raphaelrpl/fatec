a = 80000
b = 200000
anos = 0
while a <= b:
    a += (a * 3)/100
    b += (b * 1.5)/100
    anos += 1
print('A: %.0f habitantes.' % a)
print('B: %.0f habitantes.' % b)
print('Serao necessarios %.0f anos.' %anos)
