num = int(input('Informe o numero: '))
fib, aux = 0, 1
for x in range(num):
    fib, aux = aux, fib + aux

print(fib)
