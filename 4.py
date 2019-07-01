'''
Questão 04. Implemente uma solução de força bruta para o SUBSET-SUM.
            Use a instância criada na questão anterior como entrada.

    Ref: https://github.com/cdvasconcellos/PAA/blob/master/Exemplos/subsetSum.c
'''

import time

start = time.time()


def subsetSum(v: list, k: int, n: int, t: int, res: list) -> list:
    '''
        Solução de forca bruta para o problema SUBSET-SUM.

        Parameters:
            v - vetor com as combinações possíveis
            k e n - numero de elementos do vetor (k sera decrescido em cada chamada recursiva
            t - valor do somatório
            res - vetor para acumular instâncias válidas
    '''
    aux, s, i = 0, 0, 0

    print(
        f'Executando... {len(res)} soluções encontradas - {round(time.time()-start,1)} segundos', end='\r')

    if (k > 0):
        res = subsetSum(v, k-1, n, t, res)
        aux = v[n-k]
        # Atribui valor zero a posicao p/ que o elemento não seja considerado na solucao.
        v[n-k] = 0
        res = subsetSum(v, k-1, n, t, res)
        v[n-k] = aux

    else:
        s = 0
        current = []
        for i in range(n):
            s += v[i]
            if (v[i] != 0):
                current.append(v[i])
        if (s == t):
            res.append(current)

    return res


def main():

    print("# # Força bruta para SUBSET-SUM")
    print("# # Utiliza como base uma instância não satisfazível do 3-CNF-SAT reduzida para SUBSET-SUM")

    # set de valores (contempla todas as combinações resultantes da redução 3-CNF-SAT para SUBSET-SUM)
    v = [10000001111, 10011110000, 1000110011, 1011001100, 101010101, 110101010,
         10000000, 20000000, 1000000, 2000000, 100000, 200000, 10000, 20000,
         1000, 2000, 100, 200, 10, 20, 1, 2]

    # resultado de t esperado para a redução
    t = 11144444444

    # armazena os subsets que satisfazem subset-sum
    res = []

    # executa a verificacao por força bruta
    res = subsetSum(v, len(v), len(v), t, res)

    # resultado
    if len(res) > 0:
        print("\nInstâncias que atendem ao SUBSET-SUM:")
        for i in range(len(res)):
            print(f"{i+1}: {res[i]}")
    else:
        print("\nNenhuma instância atende SUBSET-SUM")


main()

# 05. A implementação de força bruta para o SUBSET-SUM tem complexidade de tempo
# exponencial ao número de elementos no conjunto. É necessário testar
# cada combinação possível dentro do conjunto, e nesse caso, tendo 22 posições,
# demandaria 2ˆ22 = 4.194.304 testes.
