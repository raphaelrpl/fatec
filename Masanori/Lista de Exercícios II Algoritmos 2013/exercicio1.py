import time

date = input('Informe uma data(dd/mm/aaaa): ')
try:
    time.strptime(date, "%d/%m/%Y")
    print("%s é uma data válida." %date)
except:
    print("Não é uma data válida.")

