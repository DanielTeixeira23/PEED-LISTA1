menor = 0

for i in range(10):
    numero = int(input('Digite o número: '))
    if numero < menor:
        menor = numero
        
print('O menor número digitado foi: ', menor)