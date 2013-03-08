valorHora = float(input('Informe quanto ganha por hora: R$'))
horas = int(input('Informe quantidade de horas trabalhadas: '))
salarioBruto = valorHora * horas
impostoRenda = (salarioBruto * 11) / 100
inss = (salarioBruto * 8) / 100
sindicato = (salarioBruto * 5) / 100
print('Salario bruto: R$%.2f X %i -> R$%.2f' %(valorHora, horas, salarioBruto))
print('Imposto de Renda: R$%.2f' %impostoRenda)
print('INSS: R$%.2f' %inss)
print('Sindicato: R$%.2f' %sindicato)
print('Salario liquido: R$%.2f'
      %(salarioBruto - impostoRenda - inss - sindicato))


