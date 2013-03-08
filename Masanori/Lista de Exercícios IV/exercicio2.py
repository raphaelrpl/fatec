valor = int(input('Informe o valor: '))
pago = int(input('Informe o valor pago: '))
troco = int(pago - valor)
notas = [50, 20, 10, 5, 2, 1]
qnt_notas = [0, 0, 0, 0, 0, 0]
print('Troco a receber: R$%i' %troco)
while troco != 0:
    for i, nota in enumerate(notas):
        if troco >= nota:
            troco -= nota
            qnt_notas[i] += 1
for cont in range(6):
    print('R$%i -> %i' %(notas[cont], qnt_notas[cont]))

