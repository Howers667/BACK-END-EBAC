# Voce recebe um array de numeros inteiros meu_arrayzinho.
# Os elementos unicos de um array sao os elementos que aparecem exatamente uma vez no array
# Retorne a soma de todos os elementos unicos de meu_arrayzinho

meu_arrayzinho = [1,2,3,3,2,4,5,5]

# Como o 1  e o 4 n se repetem voce soma eles, 1 + 4 = 5.

# 1. Criar um dicionario para adcionar a chave e o valor 
# 2. Encontrar quem sao os valores que aparecem so uma vez

meu_dicionario = {}

for i in meu_arrayzinho:
    if i not in meu_dicionario:
        meu_dicionario[i] = 1
    else:
        meu_dicionario[1] += 1


# 3. Fazer a soma dos numeros q aparecem so uma vez.
soma_das_chaves = 0

for chave, valor in meu_dicionario.items():
    if valor == 1:  
        soma_das_chaves += chave

        
print(soma_das_chaves)

