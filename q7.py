maior = ''

for i in range(5):
    palavra = input('Digite a palavra: ')
    if len(palavra) > len(maior):
        maior = palavra
    
print('Maior: ', maior)