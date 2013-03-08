num = int(input('Informe o numero: '))
cont, div = 1, 0
while cont <= num:
    if num % cont == 0:
       div +=1
    cont += 1
if div == 2:
    print('é primo')
else:
    print('não é primo')
    
    
