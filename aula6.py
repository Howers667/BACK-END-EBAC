# Dada um array de inteiros, um inteiro sortudo  eh um inteiro que  tem uma frequencia  no array igual ao seu valor

meu_array =[1,1,2,3,3,3,4,4,4,5,5,6]

meu_dicionario = {}

for i in meu_array:
    if i not in meu_dicionario:
        meu_dicionario[i] = 1
    else:
        meu_dicionario[i] += 1

for chave, valor in meu_dicionario.items():
    if chave == valor:
        print(chave)


