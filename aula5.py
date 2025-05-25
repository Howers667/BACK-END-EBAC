# Dada um array  contendo n numeros distintos  no intervalo (0,n)
# Retorne o unico numero no intervalo que esta faltando no array

meu_array = [0,1,3,4,5,6,7,8,9,10]

tamanho_meu_array = len(meu_array)

soma_valores_meu_array = sum(meu_array)

soma_total = tamanho_meu_array * (tamanho_meu_array + 1) // 2

print(soma_total - soma_valores_meu_array)