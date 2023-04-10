maiores = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    maiores.append(num)
 
print('Números maiores que 10 são: ')    
for num in maiores:
    if num > 10:
        print(num)    