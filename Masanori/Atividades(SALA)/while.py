def conta():
    num = int(input('Informe um numero: '))
    cont = 0
    while cont <= num:
        if (cont % 2 == 0):
            print(str(cont) + ' é par.')
        else:
            print(str(cont) + ' é impar.')    
        cont += 1

def soma():
    n = 1
    soma = 0
    while n <= 10:
        x = int(input('Digite o %d numero: ' %n))
        soma += x
        n += 1
    print("Soma: %d" %soma)

def fatorial(num):
    if num == 1:
        return True
    return fatorial(num-1) * num

"""fat = int(input('Informe o numero: '))
print(fatorial(fat))"""

print(int(3.9+1))
        
