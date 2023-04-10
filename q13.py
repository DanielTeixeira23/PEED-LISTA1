letra = []

for i in range(5):
    palavra= input(f"Digite a {i+1}ª palavra: ")
    letra.append(palavra)
    
for palavra in letra:
    if palavra[0] == 'a' or palavra[0] == 'A':
        print(palavra)