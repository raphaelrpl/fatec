p1 = float(input('Informe a nota da P1: '))
p2 = float(input('Informe a nota da P2: '))
ep1 = float(input('Informe a nota da EP1: '))
ep2 = float(input('Informe a nota da EP2: '))
mediaProvas = (p1 + 2*p2)/3
mediaExercicios = (ep1 + 2*ep2)/3
if (mediaProvas >= 6) and (mediaExercicios >=6):
    mediaFinal = (2 * mediaProvas + mediaExercicios)/ 3
    print('Você está aprovado!\nMedia Final: %.2f ' % mediaFinal)
else:
    mediaFinal = min(mediaProvas, mediaExercicios)
    print('Media final: %.2f' %mediaFinal)
