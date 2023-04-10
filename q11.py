par = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º numero: "))
    par.append(num)
    
print('Os números pares digitados são: ') 
for num in par:    
    if num%2==0:
        print(num)