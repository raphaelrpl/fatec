vet, vet_par, vet_imp = [], [], []
for i in range(1, 21):
    vet.append(int(input('Informe %i numero: ' %i)))
    if vet[i-1] % 2 == 0:
        vet_par.append(vet[i-1])
    else:
        vet_imp.append(vet[i-1])
print(vet)
print(vet_par)
print(vet_imp)
