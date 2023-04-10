menores = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    menores.append(num)
    
print('Os números menores que 5 são: ')
for num in menores:
    if num < 5:
        print(num)   