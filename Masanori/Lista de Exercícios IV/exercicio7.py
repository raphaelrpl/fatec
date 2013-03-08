temperaturas = []
meses = '''janeiro fevereiro março abril maio junho julho
agosto setembro outubro novembro dezembro'''.split()
media = 0
for i in range(1, 13):
    temperaturas.append(float(input('Informe a temperatura do mês %i: ' %i)))
    media += temperaturas[i-1]
media /= 12
print('Media de temperatura: %.2f' %media)
for key, value in enumerate(temperaturas):
    if value > media:
        print('Ocorreu em %s uma temperatura acima da média'
              %(meses[key], media))


