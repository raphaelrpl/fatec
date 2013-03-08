excesso = 0
multa = 0
peso = float(input('Informe o peso total dos peixes: '))
if (peso > 50):
    print('Peso em excesso.')
    excesso = peso - 50
    multa = excesso * 4

print('Peso: %s' %peso)
print('Peso em excesso: %s' %excesso)
print('Valor da multa: R$%s' % multa)
    

    
