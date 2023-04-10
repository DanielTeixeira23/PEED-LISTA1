maior = 0

for i in range(10):
    numero = int(input('Digite o número: '))
    if numero > maior:
        maior = numero
        
print('O maior número digitado foi: ', maior)