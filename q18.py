produto = 1

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    produto *= num

print('Produto: ', produto)