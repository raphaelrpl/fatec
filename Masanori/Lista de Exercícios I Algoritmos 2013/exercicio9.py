print('\nPreço do aluguel do carro por dia: R$60.00')
print('Preço KM rodado: R$0.15\n')
qnt_km = float(input('Informe a quantidade de KM percorrido: '))
dias = int(input('Informe a quantidade de dias: '))
total = (dias * 60)+(qnt_km * 0.15)
print('\nTotal gasto(em dias) com o carro alugado: R$%.2f' %(dias*60))
print('Total gasto por KM rodado: R$%.2f' % (qnt_km * 0.15))
print('\nTotal: R$%.2f' %(total))
