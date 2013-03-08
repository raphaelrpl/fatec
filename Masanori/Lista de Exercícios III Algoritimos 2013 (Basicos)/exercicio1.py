while True:
    nota = float(input('Informe uma nota entre zero e dez: '))
    if nota < 0 or nota > 10:
        print('Erro: Nota inválida!')
    else:
        print('Nota válida!')
        break
