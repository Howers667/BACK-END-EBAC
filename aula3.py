# Dada um array de numeros inteiros, cada elemento eh dado duas vezes, encontre aquele unico

meu_arrayzinho = [1,1,2,2,3,3,4]

meu_dicionario = {}

for i in meu_arrayzinho:
    if i not in meu_dicionario:
        meu_dicionario[i] = 1
    else:
        meu_dicionario[i] += 1


for chave, valor in  meu_dicionario.items():
    if valor == 1:
        print(chave)
    