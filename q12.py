impar = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º numero: "))
    impar.append(num)

print('Os números ímpares digitados são: ')
for num in impar:
    if num%2!=0:
        print(num)