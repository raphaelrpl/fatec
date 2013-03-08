num1 = float(input('1- Informe o numero: '))
num2 = float(input('2- Informe o numero: ')) 
num3 = float(input('3- Informe o numero: ')) 

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print('%s é o maior de todos e %s menor de todos' % (num1, num3))
    else:
        print('%s é o maior de todos e %s menor de todos' % (num1, num2))
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print('%s é o maior de todos e %s menor de todos' % (num2, num3))
    else:
        print('%s é o maior de todos e %s menor de todos' % (num2, num1))
elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print('%s é o maior de todos e %s menor de todos' % (num3, num2))
    else:
        print('%s é o maior de todos e %s menor de todos' % (num3, num1))
else:
    print('Erro: existem numeros iguais.')
