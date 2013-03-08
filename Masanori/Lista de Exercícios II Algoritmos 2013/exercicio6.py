num1 = float(input('1- Informe o numero: '))
num2 = float(input('2- Informe o numero: '))
num3 = float(input('3- Informe o numero: '))
if num1 > num2 and num1 > num3:
    print('%f é o maior de todos.' % num1)
elif num2 > num1 and num2 > num3:
    print('%f é o maior de todos.' % num2)
elif num3 > num1 and num3 > num2:
    print('%f é o maior de todos.' % num3)
else:
    print('Erro: existem numeros iguais.')
