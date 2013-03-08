num1 = int(input('Informe o numero: '))
num2 = int(input('Informe outro numero: '))
aux1 = num1
aux2 = num2
resto = 0
while aux1 % aux2 != 0:
    resto = aux1 % aux2
    aux1, aux2 = aux2, resto

print("O Maximo dividor entre %i e %i é %i" %(num1, num2, aux2))
