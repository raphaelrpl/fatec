cigarros = int(input('Quantos cigarros você fuma por dia?\n'))
anos = int(input('Há quantos anos você fuma?\n'))
total = ((cigarros * 365)* anos)* 10
print('Fumando %i cigarro(s) em %i ano(s), você perdeu %.2f dias de vida'
      %(int(cigarros), anos, total/60/24)
      )
