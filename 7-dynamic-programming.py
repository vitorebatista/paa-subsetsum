# 07. Implemente uma solução de programação dinâmica para o SUBSET-SUM.


def subsetsum(s: list, t: int) -> bool:
    '''
        Solução de programação dinâmica para o SUBSET-SUM

        Parameters:
            s: conjunto de inteiros positivos
            t: valor do somatório que se deseja alcançar
    '''
    lenList = len(s)
    subset = [[False] * (t + 1) for i in range(lenList + 1)]
    subset[lenList][0] = True

    for i in range(lenList-1, -1, -1):
        subset[i][0] = True
        for j in range(1, s[i]):
            subset[i][j] = subset[i+1][j]
        for j in range(s[i], t+1):
            subset[i][j] = subset[i+1][j] or subset[i+1][j - s[i]]

    return subset[0][t]


print("# # Programação Dinâmica para SUBSET-SUM")

s = [2, 4, 7, 8, 9, 10, 15, 19, 21]
t = 35
exist = subsetsum(s, t)

print(
    f"Dado um conjunto de inteiros positivos, representados como um arranjo s = {s} e um inteiro t = {t}\n")
print("Resultado:")
if (exist):
    print(f"Existe algum subconjunto de S tal que a soma de seus elementos seja t")
else:
    print(f"Não existe nenhum subconjunto de S tal que a soma de seus elementos seja t")

# R: A complexidade de tempo do algoritmo SUBSET-SUM utilizando programação dinâmica é O(n.t),
# onde n é o número de elementos do conjunto e t o valor do somatório que se deseja alcançar.
# A complexidade é polinomial ao valor de t, e exponencial ao número de dígitos de t
# pois considerando que para um t=99 (2 dígitos) são calculadas 10 linhas, para um t=100
# (3 dígitos) são calculadas 100 linhas - o que indica que é um problema pseudopolinomial.
