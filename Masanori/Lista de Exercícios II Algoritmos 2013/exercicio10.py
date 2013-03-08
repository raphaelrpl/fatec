p1 = float(input('Informe a nota P1: '))
p2 = float(input('Informe a nota P2: '))
p = (p1 + 2 * p2)/3
if p1 <= 6:
    novoP1 = float(input('Informe a nova nota P1: '))
    if novoP1 >= 7:
        print('O aluno que adotou teve um acrescimo de %.2f ponto(s).'%((p2 - novoP1)/4))
    else:
        print('O aluno que adotou não ganhou acréscimo.')
else:
    print('Sua nota ja esta aprovada!')
