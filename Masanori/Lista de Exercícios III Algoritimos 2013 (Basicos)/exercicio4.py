num = int(input('Informe o numero: '))
contador = 1
fibonacci = 1
while contador <= num:
    fibonacci += contador
    contador += 1

print('Fibonacci de %i: %i' %(num, fibonacci))
