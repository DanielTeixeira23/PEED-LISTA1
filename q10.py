soma = 0
media = 0

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    soma+=num
    
media = soma/5

print('Média: ', media)