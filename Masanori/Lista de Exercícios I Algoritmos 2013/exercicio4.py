salario = float(input('Informe o salário: '))
aumento = float(input('Informe a % do aumento: '))

total = (salario*aumento)/100

print('\n%.2f de R$%.2f é R$%.2f' %(aumento,salario, total))
print('\nNovo salário: R$%.2f' % (salario+total))
                
