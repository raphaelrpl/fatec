valor = int(input('Informe o valor total: '))
pago = int(input('Informe o valor pago: '))
notas = {50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0,}
troco = pago - valor
quitou = False
while not quitou:
    if troco >= 50:
        troco -= 50
        notas[50] += 1
    elif troco >= 20 and troco <= 49:
        troco -= 20
        notas[20] += 1
    elif troco >= 10 and troco <= 19:
        troco -= 10
        notas[10] += 1
    elif troco >= 5 and troco <= 9:
        troco -= 5
        notas[5] += 1
    elif troco >= 2 and troco <= 4:
        troco -= 2
        notas[2] += 1
    elif troco == 1:
        troco -= 1
        notas[1] += 1
    else:
        quitou = True
for nota in notas.keys():
    print('Nota de %i: %i' %(nota, notas[nota]))
