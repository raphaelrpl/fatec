lista = []
for i in range(1, 11):
    lista.append(int(input('Informe o %i numero: '%i)))
lista.sort()
print('Maior elemento -> %i\nMenor elemento: %i' %(lista[9], lista[0]))

