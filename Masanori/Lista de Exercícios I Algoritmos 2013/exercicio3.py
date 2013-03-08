dias = int(input('Informe quantos dias: '))
horas = int(input('Informe quantas horas: '))
minutos = int(input('Informe quantos minutos: '))
segundos = int(input('Informe quantos segundos: '))

total = (dias*24*60*60)+(horas*60*60)+ (minutos*60)+ segundos
print('\n%s dia(s) %s hora(s) %s minuto(s) %s segundo(s) contém %s segundos'
      % (dias, horas, minutos, segundos, total))
