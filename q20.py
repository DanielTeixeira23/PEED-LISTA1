decrescente = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    decrescente.append(num)
    
decrescente.sort(reverse=True)

print('Números em ordem decrescente: ', decrescente)