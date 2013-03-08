num = int(input('Informe o numero: '))
cont = 1
while cont <= num:
    if cont*(cont+1)*(cont+2) == num:
        print('%i é um número triangular.' %num)
        break
    elif cont == num:
        print('%i não é um número triangular.' %num)
    cont +=1
