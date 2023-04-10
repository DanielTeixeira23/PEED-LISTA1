crescente = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    crescente.append(num)
    
crescente.sort()

print('Números em ordem crescente: ', crescente)