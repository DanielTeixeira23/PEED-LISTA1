soma = 0

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    
    if num%2==0:
        soma += num
        
print('O produto dos números pares é: ', soma)        