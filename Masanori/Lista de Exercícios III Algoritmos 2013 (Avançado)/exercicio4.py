num = int(input('Informe o numero: '))
resultado = num
dicionario = {}
fator = 2
while not resultado == 1:
    quantidade = 0
    if resultado % fator == 0:
        quantidade += 1
        resultado /= fator
        if fator in dicionario.keys():
            dicionario[fator]+= 1
        else:
            dicionario.update({ fator:quantidade })
    else:
        fator += 1
for dados in dicionario:
    print('O fator %i apareceu %i veze(s).' %(dados, dicionario[dados]))
