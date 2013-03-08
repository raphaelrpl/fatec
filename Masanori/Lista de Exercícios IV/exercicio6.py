altura, idade = [], []
media = 0
for i in range(1, 31):
    altura.append(float(input('Informe a altura do aluno %i: ' %i)))
    idade.append(float(input('Informe a idade do aluno %i: ' %i)))
    media += altura[i-1]
media /= 30
qnt = 0
for key, value in enumerate(idade):
    if value >= 13 and altura[key] < media:
        qnt += 1
print('São %i aluno(s) que possuem altura inferior %.2f' %(qnt, media))
        
