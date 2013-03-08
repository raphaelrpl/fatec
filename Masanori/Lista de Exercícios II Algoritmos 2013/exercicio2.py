lado1 = float(input('Informe o valor do Lado 1 do triangulo: '))
lado2 = float(input('Informe o valor do Lado 2 do triangulo: '))
lado3 = float(input('Informe o valor do Lado 3 do triangulo: '))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Valor invalido em um dos lados!")
elif lado1+lado2 > lado3 and lado1+lado3 > lado2 and lado2+lado3 > lado1:
    if (lado1 == lado2) and (lado1 == lado3):
        print('É um triangulo equilatero.')
    elif(lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print('É um triangulo isóceles.')
    else:
        print('É um triangulo escaleno.')
else:
    print('Não forma um triangulo')

    
